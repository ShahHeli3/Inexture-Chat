import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

# from chat.models import Message
from chat.models import Room, Message
from users.models import CustomUser


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # save message in the database
    def save_message(self, message, sender_user_id, message_type):
        sender_user = CustomUser.objects.get(id=sender_user_id)
        room = Room.objects.get(room_name=self.room_name)
        new_message = Message.objects.create(sender_user=sender_user, room=room, message=message,
                                             message_type=message_type)
        new_message.save()

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_user = text_data_json['sender_user']
        sender_user_id = text_data_json['sender_user_id']
        message_type = text_data_json['message_type']
        self.save_message(message, sender_user_id, message_type)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_user': sender_user,
                'message_type': message_type,
                'sender_user_id': sender_user_id
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        sender_user = event['sender_user']
        message_type = event['message_type']
        sender_user_id = event['sender_user_id']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'sender_user': sender_user,
            'message_type': message_type,
            'sender_user_id': sender_user_id
        }))
