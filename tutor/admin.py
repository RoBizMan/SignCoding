from django.core.exceptions import PermissionDenied
from django.contrib import admin, messages
from .models import Tutor, ProgrammingLanguage, SignLanguage, DayAvailability, TimeSlot
from .forms import TutorAdminForm


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Tutor model. This class controls how tutors are displayed and managed in the Django admin interface.

    - `form`: Specifies a custom form (`TutorAdminForm`) to handle validation logic for Many-to-Many fields.
        The form ensures that at least one option is selected for programming languages, sign languages, day availability,
        and time availability before a tutor can be saved. This prevents empty selections that would otherwise cause validation errors.
    
    - `list_display`: Specifies which fields will be displayed in the list view of tutors, including first name, last name, email, and price.
    
    - `search_fields`: Allows searching tutors by their first name, last name, or email, making it easier to find specific tutors.
    
    - `list_filter`: Enables filtering tutors by their associated programming languages, sign languages, day availability, and time availability.
        This helps to narrow down results based on these categories.

    - `filter_horizontal`: Provides an interface for easily selecting multiple Many-to-Many relationships like programming languages, sign languages,
        and time availability. This allows for a more user-friendly selection process in the admin view.

    The `TutorAdminForm` ensures that the admin interface validates the `ManyToMany` fields and prevents saving a tutor profile without
        selecting at least one item from these fields.
    """
    form = TutorAdminForm  # Use the custom form for validation of Many-to-Many fields
    list_display = ('tutor_firstname', 'tutor_lastname', 'tutor_email', 'price')  # Display these fields in the list view
    search_fields = ('tutor_firstname', 'tutor_lastname', 'tutor_email')  # Add search functionality
    list_filter = ('programming_languages', 'sign_languages', 'day_availability', 'time_availability')  # Add filters for better navigation

    # Use boxes to manage multiple selections easier in the admin view
    filter_horizontal = ('programming_languages', 'sign_languages', 'time_availability')


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ProgrammingLanguage model. This controls the 
    management of programming languages in the Django admin interface.
    
    - `list_display`: Displays the name of each programming language in the list view.
    - `search_fields`: Allows searching for a specific programming language by name.
    - `has_delete_permission`: Prevents deletion of programming languages if they are associated with any tutor.
    """
    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of programming languages that are associated with tutors.
        Displays a custom error message if a language is in use by any tutor.
        """
        if obj:
            associated_tutors = Tutor.objects.filter(programming_languages=obj)
            if associated_tutors.exists():
                message = (
                    f"Cannot delete '{obj.name}' because it is associated with tutors. "
                    "Please remove this language from all associated tutors before deleting it."
                )
                self.message_user(request, message, level=messages.ERROR)
                return False  # Prevent deletion and show the custom message
        
        # Proceed with default behavior if no condition matches
        return super().has_delete_permission(request, obj)


@admin.register(SignLanguage)
class SignLanguageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SignLanguage model. This controls the management of 
    sign languages in the Django admin interface.

    - `list_display`: Displays the name of each sign language in the list view.
    - `search_fields`: Allows searching for a specific sign language by name.
    - `has_delete_permission`: Prevents deletion of sign languages if they are associated with any tutor.
    """
    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of sign languages that are associated with tutors.
        Displays a custom error message if a language is in use by any tutor.
        """
        if obj:
            associated_tutors = Tutor.objects.filter(sign_languages=obj)
            if associated_tutors.exists():
                message = (
                    f"Cannot delete '{obj.name}' because it is associated with tutors. "
                    "Please remove this language from all associated tutors before deleting it."
                )
                self.message_user(request, message, level=messages.ERROR)
                return False  # Prevent deletion and show the custom message
        
        # Proceed with default behavior if no condition matches
        return super().has_delete_permission(request, obj)


@admin.register(DayAvailability)
class DayAvailabilityAdmin(admin.ModelAdmin):
    """
    Admin configuration for the DayAvailability model. This manages the list of 
    predefined days (Monday to Sunday) when a tutor can be available. The list of 
    days is fixed and cannot be modified by the admin user.

    - `list_display`: Displays the name of the day.
    - `get_queryset`: Limits the list to predefined days (Monday through Sunday).
    - `has_add_permission`, `has_delete_permission`, `has_change_permission`: 
    
    All permissions are restricted to prevent adding, deleting, or changing days.
    """
    list_display = ('name',)
    search_fields = ('name',)

    def get_queryset(self, request):
        """
        Limits the queryset to only the predefined days of the week.
        """
        return super().get_queryset(request).filter(name__in=[
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ])

    def has_add_permission(self, request):
        """
        Prevent adding new day entries to ensure the list of days is fixed.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of predefined days.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Prevent modification of existing days.
        """
        return False


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TimeSlot model. This controls the management of time slots 
    available for tutors, and prevents the deletion of time slots associated with tutors.

    - `list_display`: Displays formatted start and end times for each time slot.
    - `search_fields`: Allows searching by start and end times.
    - `has_delete_permission`: Prevents deletion of time slots that are associated with any tutor.
    """
    list_display = ('formatted_start_time', 'formatted_end_time')
    search_fields = ('start_time', 'end_time')

    def formatted_start_time(self, obj):
        """
        Returns the start time formatted as HH:MM.
        """
        return obj.start_time.strftime('%H:%M') # Returns as 24-hours time format
    formatted_start_time.short_description = 'Start Time'

    def formatted_end_time(self, obj):
        """
        Returns the end time formatted as HH:MM.
        """
        return obj.end_time.strftime('%H:%M') # Returns as 24-hours time format
    formatted_end_time.short_description = 'End Time'

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of time slots that are associated with tutors.
        Displays a custom error message if a time slot is in use by any tutor.
        """
        if obj:
            associated_tutors = Tutor.objects.filter(time_availability=obj)
            if associated_tutors.exists():
                message = (
                    f"Cannot delete '{obj.start_time.strftime('%H:%M')} - {obj.end_time.strftime('%H:%M')}' because it is associated with tutors. "
                    "Please remove this time slot from all associated tutors before deleting it."
                )
                self.message_user(request, message, level=messages.ERROR)
                return False  # Prevent deletion and show the custom message
        
        # Proceed with default behavior if no condition matches
        return super().has_delete_permission(request, obj)
