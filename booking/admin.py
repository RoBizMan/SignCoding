from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Booking model.
    """
    list_display = ('booking_id', 'user', 'tutor', 'total_price', 'session_date', 'time_slot', 'booking_date')
    list_filter = ('session_date', 'user', 'tutor')
    search_fields = ('booking_id', 'user__personal_firstname', 'user__personal_lastname', 'tutor__tutor_firstname', 'tutor__tutor_lastname')
    ordering = ('-booking_date',)

    # Read-only fields to prevent modification
    readonly_fields = ('booking_id', 'booking_date', 'stripe_pid')

    # Add the ability to filter bookings by user and tutor
    fieldsets = (
        (None, {
            'fields': ('booking_id', 'booking_date', 'stripe_pid', 'user', 'tutor', 'total_price', 'session_date', 'time_slot')
        }),
    )


# Register the Booking model with the custom admin configuration
admin.site.register(Booking, BookingAdmin)
