from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Represents a user profile that extends the default User model.

    This model allows for additional user information to be stored
    alongside the default User model provided by Django. Each profile
    is associated with a unique user account.

    Attributes:
        personal_details (OneToOneField): The user associated with this
            profile, linked to the User model.
        personal_firstname (CharField): User's first name, optional.
        personal_lastname (CharField): User's last name, optional.
    """

    personal_details = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Username"
    )
    personal_firstname = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="User's First Name"
    )
    personal_lastname = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="User's Last Name"
    )

    def __str__(self):
        """Returns the username associated with this profile."""
        return self.personal_details.username

    def get_full_name(self):
        """
        Returns the full name of the user by combining first and last names.

        Returns:
            str: The full name of the user.
        """
        return f"{self.personal_firstname} {self.personal_lastname}".strip()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Ensures a Profile is created or updated whenever a User is saved.

    This signal handler listens for the post_save signal from the User
    model. It creates a new Profile when a new User is created and
    updates the Profile when an existing User's details are modified.

    Args:
        sender (Model): The model that sent the signal (User).
        instance (User): The instance of the User that was saved.
        created (bool): Indicates whether a new instance was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        # Create a new Profile for the newly created User
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
