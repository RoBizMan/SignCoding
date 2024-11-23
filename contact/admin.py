from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'full_name', 'email', 'date_submitted')
    search_fields = ('full_name', 'email', 'ticket_id')
    list_filter = ('date_submitted',)
