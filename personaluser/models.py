from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    """
    Represents a user profile that extends the default User model.
    
    Attributes:
    personal_details (OneToOneField): The user associated with this profile.
    personal_firstname (CharField): User's first name.
    personal_lastname (CharField): User's last name.
    """
    personal_details = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_firstname = models.CharField(max_length=50, blank=True, null=True)
    personal_lastname = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.personal_details.username}'s Profile"  # Use personal_details instead of user

# Signal to create a Profile instance when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(personal_details=instance)  # Use personal_details here

# Signal to save the Profile instance when the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # This will work if you rename the OneToOneField
