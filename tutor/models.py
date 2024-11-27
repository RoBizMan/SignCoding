from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from cloudinary.models import CloudinaryField


class ProgrammingLanguage(models.Model):
    """
    Handles the list of programming languages for the Tutor model.

    This model allows adding or deleting programming languages
    that tutors can teach.

    Attributes:
        name (CharField): The name of the programming language,
                            must be unique.
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SignLanguage(models.Model):
    """
    Handles the list of sign languages for the Tutor model.

    This model allows adding or deleting sign languages that
    tutors can communicate in.

    Attributes:
        name (CharField): The name of the sign language, must be unique.
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class DayAvailability(models.Model):
    """
    Represents the availability of tutors on specific days.

    This model maintains a fixed list of days (e.g., Monday to
    Sunday) that cannot be modified. Tutors select their available
    days from this predefined list.

    Attributes:
        name (CharField): The name of the day, must be unique.
        order (PositiveIntegerField): The order in which to display
                                        the days.
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

    This model indicates when a tutor is available for sessions.
    Tutors can select time slots from a predefined set.

    Attributes:
        start_time (TimeField): The starting time of the slot.
        end_time (TimeField): The ending time of the slot.

    Methods:
        __str__(): Returns the time range as a string in 24-hour format.
        clean(): Validates that the start time is before the end time.
    """

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        """Returns a formatted string representation of the time slot."""
        return (
            f"{self.start_time.strftime('%H:%M')} - "
            f"{self.end_time.strftime('%H:%M')}"
        )

    def clean(self):
        """Validates that start time is before end time."""
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")


class Tutor(models.Model):
    """
    Represents a tutor profile.

    This model stores information about tutors and maintains
    relationships with programming languages, sign languages,
    day availability, and time slots.

    Attributes:
        tutor_firstname (CharField): Tutor's first name.
        tutor_lastname (CharField): Tutor's surname.
        tutor_email (EmailField): Tutor's email address, validated using
                                    EmailValidator.
        programming_languages (ManyToManyField): Languages the tutor can teach.
        sign_languages (ManyToManyField): Sign languages the tutor knows.
        day_availability (ManyToManyField): Days when the tutor is available.
        time_availability (ManyToManyField): Time slots when the
                                                tutor is available.
        price (DecimalField): Tutor’s hourly rate.
        photo (CloudinaryField): Profile photo of the tutor,
                                    with a default image.

    Methods:
        __str__(): Returns a string representation of the tutor profile,
                    including first name, last name, and email.
        get_full_name(): Returns the full name of the tutor.
    """

    tutor_firstname = models.CharField(
        max_length=50, verbose_name="Tutor's First Name"
    )
    tutor_lastname = models.CharField(
        max_length=50, verbose_name="Tutor's Surname"
    )
    tutor_email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Tutor's Email Address",
        validators=[EmailValidator()]
    )
    programming_languages = models.ManyToManyField(
        ProgrammingLanguage, related_name="tutors"
    )
    sign_languages = models.ManyToManyField(
        SignLanguage, related_name="tutors"
    )
    day_availability = models.ManyToManyField(DayAvailability)
    time_availability = models.ManyToManyField(TimeSlot, related_name="tutors")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = CloudinaryField(
        'profile_picture', default='images/default_tutor.jpg'
    )

    def __str__(self):
        """Returns a string representation of the tutor profile."""
        return (
            f"{self.tutor_firstname} {self.tutor_lastname} | "
            f"{self.tutor_email}"
        )

    def get_full_name(self):
        """Returns the full name of the tutor."""
        return f"{self.tutor_firstname} {self.tutor_lastname}"
