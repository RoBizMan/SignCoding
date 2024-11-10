from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class SignLanguage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class DayAvailability(models.Model):
    name = models.CharField(max_length=20, unique=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Day Availability"
        verbose_name_plural = "Day Availabilities"


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"


class Tutor(models.Model):
    tutor_firstname = models.CharField(max_length=50, verbose_name="Tutor's First Name")
    tutor_lastname = models.CharField(max_length=50, verbose_name="Tutor's Surname")
    tutor_email = models.EmailField(max_length=254, unique=True, verbose_name="Tutor's Email Address")
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    sign_languages = models.ManyToManyField(SignLanguage)
    day_availability = models.ManyToManyField(DayAvailability)
    time_availability = models.ManyToManyField(TimeSlot)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='tutor_images/', default='tutor_images/default.jpg')
    
    def __str__(self):
        return f"{self.tutor_firstname} {self.tutor_lastname} | {self.tutor_email}"