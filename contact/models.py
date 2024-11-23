from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.full_name}"
