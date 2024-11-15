# Generated by Django 5.1.2 on 2024-11-13 18:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaluser', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='personal_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='personal_firstname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="User's First Name"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='personal_lastname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="User's Last Name"),
        ),
    ]
