from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.

    This class customizes the admin interface for managing user
    profiles. It allows displaying key fields in the admin list
    view and provides search functionality.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to search by in the admin interface.
    """

    list_display = (
        'personal_details', 'personal_firstname', 'personal_lastname'
    )
    search_fields = (
        'personal_details__username', 'personal_firstname', 'personal_lastname'
    )


# Register the Profile model with the custom admin configuration
admin.site.register(Profile, ProfileAdmin)
