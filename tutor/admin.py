from django.contrib import admin
from .models import Tutor, ProgrammingLanguage, SignLanguage, DayAvailability, TimeSlot

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_firstname', 'tutor_lastname', 'tutor_email', 'price')  # Display these fields in the list view
    search_fields = ('tutor_firstname', 'tutor_lastname', 'tutor_email')  # Add search functionality
    list_filter = ('programming_languages', 'sign_languages', 'day_availability')  # Add filters for better navigation

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SignLanguage)
class SignLanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(DayAvailability)
class DayAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def get_queryset(self, request):
        # Limit queryset to only the predefined days
        return super().get_queryset(request).filter(name__in=[
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ])

    def has_add_permission(self, request):
        # Prevent adding new entries
        return False

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of existing entries
        return False

    def has_change_permission(self, request, obj=None):
        # Allow changing existing entries if needed
        return False

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('formatted_start_time', 'formatted_end_time')
    search_fields = ('start_time', 'end_time')

    def formatted_start_time(self, obj):
        return obj.start_time.strftime('%H:%M')
    formatted_start_time.short_description = 'Start Time'

    def formatted_end_time(self, obj):
        return obj.end_time.strftime('%H:%M')
    formatted_end_time.short_description = 'End Time'
