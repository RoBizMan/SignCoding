from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Booking model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Fields to filter bookings in the admin view.
        search_fields (tuple): Fields to search bookings by.
        ordering (tuple): Default ordering for bookings.
        readonly_fields (tuple): Fields that cannot be modified in the admin.
        fieldsets (tuple): Grouping of fields in the admin form.
    """

    list_display = (
        'booking_id', 'booking_date', 'user_fullname',
        'user_email', 'tutor_fullname', 'tutor_email',
        'total_price', 'session_date'
    )
    list_filter = ('session_date', 'booking_date')
    search_fields = (
        'booking_id', 'user__personal_firstname',
        'user__personal_lastname',
        'tutor__tutor_firstname',
        'tutor__tutor_lastname'
    )
    ordering = ('-booking_date',)

    # Read-only fields to prevent modification
    readonly_fields = (
        'booking_id', 'booking_date', 'stripe_pid',
        'user_fullname', 'user_email',
        'tutor_fullname', 'tutor_email',
        'total_price', 'session_date',
        'session_time'
    )

    # Fieldsets for grouping fields in the admin form
    fieldsets = (
        (None, {
            'fields': (
                'booking_id', 'booking_date', 'stripe_pid',
                'user_fullname', 'user_email',
                'tutor_fullname', 'tutor_email',
                'total_price', 'session_date',
                'session_time'
            )
        }),
    )


# Register the Booking model with the custom admin configuration
admin.site.register(Booking, BookingAdmin)
