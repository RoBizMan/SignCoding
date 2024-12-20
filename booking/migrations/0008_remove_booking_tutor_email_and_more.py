# Generated by Django 5.1.2 on 2024-11-23 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_booking_tutor_email_booking_tutor_full_name_and_more'),
        ('personaluser', '0002_alter_profile_personal_details_and_more'),
        ('tutor', '0008_alter_tutor_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='tutor_email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='tutor_full_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_full_name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='tutor.tutor'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='personaluser.profile'),
        ),
    ]
