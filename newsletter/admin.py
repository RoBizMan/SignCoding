from django.contrib import admin
from .models import NewsletterSubscription


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NewsletterSubscription model.

    This class customizes the admin interface for managing newsletter
    subscriptions. It allows displaying key fields in the admin list
    view.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """

    list_display = ('email',)  # Display the email address of subscribers
