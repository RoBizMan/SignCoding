from django.db import models


class NewsletterSubscription(models.Model):
    """
    Represents a subscription to the newsletter.

    This model stores the email addresses of users who have subscribed
    to the newsletter. Each subscription is uniquely identified by
    the email address.

    Attributes:
        email (EmailField): The email address of the subscriber, which
                            must be unique across all subscriptions.

    Methods:
        __str__(): Returns the email address of the subscriber as a
                    string representation of the model instance.
    """

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
