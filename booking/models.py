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
    - booking_id (CharField): Unique identifier for the booking.
    - booking_date (DateTimeField): Timestamp of when the booking was made.
    - stripe_pid (CharField): Stripe's unique transaction ID for payment tracking.
    - user (ForeignKey to :model:`personaluser.Profile`): The user who made the booking.
    - tutor (ForeignKey to :model:`tutor.Tutor`): The tutor assigned to the booking.
    - total_price (DecimalField): Total price for the tutoring session.
    - session_date (DateField): The date of the tutoring session.
    - session_time (ManyToManyField to :model:`tutor.TimeSlot`): The time slot selected for the tutoring session.
    """
    booking_id = models.CharField(max_length=32, unique=True, editable=False, verbose_name="Booking ID")
    booking_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Booking Date")
    stripe_pid = models.CharField(max_length=254, unique=True, null=False, blank=False, default='', editable=False, verbose_name="Stripe Payment ID")
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="bookings")
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name="bookings")
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    session_date = models.DateField()
    session_time = models.ManyToManyField(TimeSlot, related_name="bookings")

    class Meta:
        ordering = ['-booking_date']

    def _generate_booking_id(self):
        """
        Generate a random, unique booking ID using UUID.
        """
        return uuid.uuid4().hex.upper()

    def _generate_stripe_pid(self):
        """
        Generate a unique dummy Stripe Payment ID (typically you would get this from Stripe after the payment).
        """
        # For the sake of this example, generate a unique UUID as the dummy Stripe PID
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the save method to set a unique booking ID and Stripe PID
        if they have not been set already.
        """
        if not self.booking_id:
            self.booking_id = self._generate_booking_id()

        if not self.stripe_pid:  # Ensure a unique Stripe PID is always generated
            self.stripe_pid = self._generate_stripe_pid()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking Number {self.booking_id}"

    def is_available(tutor, session_date, time_slot):
        """
        Check if the tutor is available for the given session date and time slot.
        """
        bookings = Booking.objects.filter(
            tutor=tutor,
            session_date=session_date,
            session_time=time_slot
        )
        return not bookings.exists()
