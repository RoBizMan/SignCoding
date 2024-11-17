# Generated by Django 5.1.2 on 2024-11-17 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personaluser', '0002_alter_profile_personal_details_and_more'),
        ('tutor', '0005_alter_tutor_price_alter_tutor_tutor_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(editable=False, max_length=32, unique=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('stripe_pid', models.CharField(default='', editable=False, max_length=254)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('session_date', models.DateField()),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='tutor.timeslot')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='tutor.tutor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='personaluser.profile')),
            ],
        ),
    ]
