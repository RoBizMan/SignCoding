from django.db import models
import uuid
from datetime import date
from tutor.models import Tutor, TimeSlot, DayAvailability
from personaluser.models import Profile


# Create your models here.
class Booking(models.Model):
    """
    Represents a tutoring session booking.

    Attributes:
    - booking_id (CharField): Unique identifier for the booking,
        automatically generated using UUID.
    - booking_date (DateTimeField): Timestamp of when the booking was
        made, set automatically on creation.
    - stripe_pid (CharField): Stripe's unique transaction ID for payment
        tracking, ensuring each transaction is identifiable.
    - user (ForeignKey to :model:`personaluser.Profile`): The user who
        made the booking, linked to their profile.
    - user_fullname (CharField): Full name of the user making the
        booking, stored for display purposes.
    - user_email (CharField): Email address of the user making the
        booking, used for communication and notifications.
    - tutor (ForeignKey to :model:`tutor.Tutor`): The tutor assigned to
        the booking, linking to the Tutor model.
    - tutor_fullname (CharField): Full name of the assigned tutor,
        stored for display purposes.
    - tutor_email (CharField): Email address of the assigned tutor,
        used for communication and notifications.
    - total_price (DecimalField): Total price for the tutoring session,
        stored as a decimal value with two decimal places.
    - session_date (DateField): The date of the tutoring session,
        indicating when the session will occur.
    - session_time (ManyToManyField to :model:`tutor.TimeSlot`): The
        time slot(s) selected for the tutoring session, allowing for
        flexibility in scheduling.

    Methods:
    - _generate_booking_id(): Generates a random, unique booking ID
        using UUID.
    - save(): Overrides the default save method to ensure a unique
        booking ID and Stripe PID are set before saving.
    - __str__(): Returns a string representation of the Booking instance,
        showing the booking number.
    - is_available(tutor, session_date, time_slot): Checks if the
        specified tutor is available for the given session date and time
        slot.
    """

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]

    booking_id = models.CharField(
        max_length=32, unique=True,
        editable=False,
        verbose_name="Booking ID"
    )
    booking_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="Booking Date"
    )
    stripe_pid = models.CharField(
        max_length=254, unique=True,
        null=False, blank=False,
        default='', editable=False,
        verbose_name="Stripe Payment ID"
    )
    user = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        related_name="bookings", null=True
    )
    user_fullname = models.CharField(
        max_length=101, null=True,
        blank=False,
        verbose_name="User's Full Name"
    )
    user_email = models.CharField(
        max_length=254, null=True,
        blank=False,
        verbose_name="User's Email address"
    )
    tutor = models.ForeignKey(
        Tutor, on_delete=models.SET_NULL,
        related_name="bookings", null=True
    )
    tutor_fullname = models.CharField(
        max_length=101, null=True,
        blank=False,
        verbose_name="Tutor's Full Name"
    )
    tutor_email = models.CharField(
        max_length=254, null=True,
        blank=False,
        verbose_name="Tutor's Email address"
    )
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    session_date = models.DateField()
    session_time = models.ManyToManyField(
        TimeSlot, related_name="bookings"
    )
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )

    class Meta:
        ordering = ['-booking_date']

    def _generate_booking_id(self):
        """
        Generate a random, unique booking ID using UUID.
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the save method to set a unique booking ID and Stripe PID
        if they have not been set already.
        """
        if not self.booking_id:
            self.booking_id = self._generate_booking_id()

        if not self.stripe_pid:
            self.stripe_pid = self._generate_stripe_pid()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking Number {self.booking_id}"

    def is_available(tutor, session_date, time_slot):
        """
        Check if the tutor is available for the given session date and
        time slot.
        """
        bookings = Booking.objects.filter(
            tutor=tutor,
            session_date=session_date,
            session_time=time_slot
        )
        return not bookings.exists()
