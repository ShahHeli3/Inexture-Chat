# Generated by Django 4.0.6 on 2022-07-29 10:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_group_group_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_icon',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
