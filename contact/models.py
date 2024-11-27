from django.db import models
import uuid


class Contact(models.Model):
    """
    Represents a contact submission from a user.

    This model stores information submitted by users through the
    contact form, including their name, email address, and message.
    Each submission is uniquely identified by a ticket ID and
    timestamped with the date it was submitted.

    Attributes:
        ticket_id (UUIDField): A unique identifier for each contact
            submission, automatically generated using UUID.
        date_submitted (DateTimeField): The date and time when the
            contact submission was created, set automatically.
        full_name (CharField): The full name of the user submitting
            the contact form.
        email (EmailField): The email address of the user submitting
            the contact form.
        message (TextField): The message content submitted by the user.

    Methods:
        __str__(): Returns a string representation of the contact
            submission, including the ticket ID and user's full name.
    """

    ticket_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    date_submitted = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.full_name}"
