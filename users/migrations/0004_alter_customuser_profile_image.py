# Generated by Django 4.0.6 on 2022-07-29 08:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='v1659082333/profiles/cqk8qmuh9ovndjvorcai.jpg', max_length=255, verbose_name='image'),
        ),
    ]
