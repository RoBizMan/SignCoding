# Generated by Django 5.1.2 on 2024-11-18 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_tutoravailability_alter_booking_time_slot'),
        ('tutor', '0005_alter_tutor_price_alter_tutor_tutor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='booking',
            name='session_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='tutor.timeslot'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='stripe_pid',
            field=models.CharField(default='', editable=False, max_length=254, unique=True, verbose_name='Stripe Payment ID'),
        ),
        migrations.DeleteModel(
            name='TutorAvailability',
        ),
    ]
