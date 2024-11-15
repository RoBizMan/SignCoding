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
    personal_details = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Username")
    personal_firstname = models.CharField(max_length=50, blank=True, null=True, verbose_name="User's First Name")
    personal_lastname = models.CharField(max_length=50, blank=True, null=True, verbose_name="User's Last Name")

    def __str__(self):
        return f"{self.personal_details.username}'s Profile"

# Signal to create or update Profile instance when User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Ensures a Profile is created or updated whenever a User is saved.
    """
    if created:
        Profile.objects.create(
            personal_details=instance,
            personal_firstname=instance.first_name,
            personal_lastname=instance.last_name
        )
    else:
        # Update existing Profile with User's latest first and last names
        profile = Profile.objects.get(personal_details=instance)
        profile.personal_firstname = instance.first_name
        profile.personal_lastname = instance.last_name
        profile.save()
