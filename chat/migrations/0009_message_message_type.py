# Generated by Django 4.0.6 on 2022-08-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_message_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_type',
            field=models.CharField(default='text', max_length=100),
        ),
    ]
