# Generated by Django 4.0.6 on 2022-07-29 08:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_group_remove_room_receiver_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_icon',
            field=cloudinary.models.CloudinaryField(default='media/group_default.png', max_length=255, verbose_name='image'),
        ),
    ]
