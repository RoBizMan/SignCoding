from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.

    This class customizes the admin interface for managing contact
    submissions. It allows filtering, searching, and displaying key
    fields in the admin list view.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to search by in the admin interface.
        list_filter (tuple): Fields to filter contacts by in the admin view.
    """

    list_display = ('ticket_id', 'full_name', 'email', 'date_submitted')
    search_fields = ('full_name', 'email', 'ticket_id')
    list_filter = ('date_submitted',)
