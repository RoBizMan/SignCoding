# Generated by Django 5.1.2 on 2024-11-22 18:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0005_alter_tutor_price_alter_tutor_tutor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
