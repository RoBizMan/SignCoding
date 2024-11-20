from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class ProgrammingLanguage(models.Model):
    """
    Handles the list of programming languages for
    the programming languages' M2M field in the Tutor model.
    Allows adding or deleting programming languages.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SignLanguage(models.Model):
    """
    Handles the list of sign languages for
    the sign languages' M2M field in the Tutor model.
    Allows adding or deleting sign languages.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class DayAvailability(models.Model):
    """
    Handles the list of day availability for
    the day availability M2M relationship in the Tutor model.
    The list of days is fixed (e.g., Monday, Tuesday, etc.) and cannot be modified.
    Tutors select the days they are available from this predefined list.
    """
    name = models.CharField(max_length=20, unique=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Day Availability"
        verbose_name_plural = "Day Availabilities"


class TimeSlot(models.Model):
    """
    Represents a time availability slot for tutors.
    The time slots are used to indicate when a tutor is available for sessions.
    Tutors can select time slots from a predefined set.

    Attributes:
    start_time (TimeField): The starting time of the slot.
    end_time (TimeField): The ending time of the slot.

    Methods:
    __str__ (str): Returns the time range as a string in 24-hour format.
    clean: Validates that the start time is before the end time.
    """
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        # Display the 24-hours time format in the admin panel view
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

    def clean(self):
        # Prevents the admin from adding the wrong time slot
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")


class Tutor(models.Model):
    """
    Represents a tutor profile.

    Stores a tutor profile and maintains relationships with:
    - :model:`ProgrammingLanguage`: a list of programming languages the tutor is proficient in,
    - :model:`SignLanguage`: a list of sign languages the tutor can communicate in,
    - :model:`DayAvailability`: a list of days the tutor is available for work,
    - :model:`TimeSlot`: a list of time slots the tutor is available for work.

    Attributes:
    tutor_firstname (str): Tutor's first name.
    tutor_lastname (str): Tutor's surname.
    tutor_email (EmailField): Tutor's email address, validated using EmailValidator.
    programming_languages (ManyToManyField to :model:`ProgrammingLanguage`): The programming languages the tutor can teach.
    sign_languages (ManyToManyField to :model:`SignLanguage`): The sign languages the tutor knows.
    day_availability (ManyToManyField to :model:`DayAvailability`): Days when the tutor is available.
    time_availability (ManyToManyField to :model:`TimeSlot`): Time slots when the tutor is available.
    price (DecimalField): Tutor’s hourly rate.
    photo (ImageField): Profile photo of the tutor, with a default image.

    Methods:
    __str__ (str): Returns a string representation of the tutor profile, including first name, last name, and email.
    """
    tutor_firstname = models.CharField(max_length=50, verbose_name="Tutor's First Name")
    tutor_lastname = models.CharField(max_length=50, verbose_name="Tutor's Surname")
    tutor_email = models.EmailField(max_length=254, unique=True, verbose_name="Tutor's Email Address", validators=[EmailValidator()])
    programming_languages = models.ManyToManyField(ProgrammingLanguage, related_name="tutors")
    sign_languages = models.ManyToManyField(SignLanguage, related_name="tutors")
    day_availability = models.ManyToManyField(DayAvailability)
    time_availability = models.ManyToManyField(TimeSlot, related_name="tutors")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='tutor_images/', default='tutor_images/default.jpg')

    def __str__(self):
        return f"{self.tutor_firstname} {self.tutor_lastname} | {self.tutor_email}"

    def get_full_name(self):
        return f"{self.tutor_firstname} {self.tutor_lastname}"
