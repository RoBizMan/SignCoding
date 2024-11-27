from django.core.exceptions import PermissionDenied
from django.contrib import admin, messages
from .models import (
    Tutor, ProgrammingLanguage, SignLanguage, DayAvailability, TimeSlot
)
from .forms import TutorAdminForm


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Tutor model.

    This class controls how tutors are displayed and managed in the
    Django admin interface.

    Attributes:
        form (Type[forms.ModelForm]): Specifies a custom form
            (TutorAdminForm) to handle validation logic for
            Many-to-Many fields.
        list_display (tuple): Fields displayed in the list view of
            tutors.
        search_fields (tuple): Fields to search by in the admin
            interface.
        list_filter (tuple): Enables filtering tutors by associated
            programming languages, sign languages, day availability,
            and time availability.
        filter_horizontal (tuple): Provides an interface for easily
            selecting multiple Many-to-Many relationships.
    """

    form = TutorAdminForm  # Custom form for validation of Many-to-Many fields
    list_display = (
        'tutor_firstname', 'tutor_lastname', 'tutor_email', 'price'
    )
    search_fields = ('tutor_firstname', 'tutor_lastname', 'tutor_email')
    list_filter = (
        'programming_languages', 'sign_languages',
        'day_availability', 'time_availability'
    )
    filter_horizontal = (
        'programming_languages', 'sign_languages', 'time_availability'
    )


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ProgrammingLanguage model.

    This controls the management of programming languages in the
    Django admin interface.

    Attributes:
        list_display (tuple): Displays the name of each programming
            language in the list view.
        search_fields (tuple): Allows searching for a specific
            programming language by name.
    """

    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of programming languages that are associated
        with tutors.

        Args:
            request (HttpRequest): The HTTP request object.
            obj (Optional[ProgrammingLanguage]): The instance being deleted.

        Returns:
            bool: False if the language is in use by any tutor, else True.
        """
        if obj:
            associated_tutors = Tutor.objects.filter(programming_languages=obj)
            if associated_tutors.exists():
                message = (
                    f"Cannot delete '{obj.name}' because it is associated "
                    "with tutors. Please remove this language from all "
                    "associated tutors before deleting it."
                )
                self.message_user(request, message, level=messages.ERROR)
                return False  # Prevent deletion and show the custom message

        return super().has_delete_permission(request, obj)


@admin.register(SignLanguage)
class SignLanguageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SignLanguage model.

    This controls the management of sign languages in the Django admin
    interface.

    Attributes:
        list_display (tuple): Displays the name of each sign language
            in the list view.
        search_fields (tuple): Allows searching for a specific sign
            language by name.
    """

    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of sign languages that are associated with tutors.

        Args:
            request (HttpRequest): The HTTP request object.
            obj (Optional[SignLanguage]): The instance being deleted.

        Returns:
            bool: False if the language is in use by any tutor, else True.
        """
        if obj:
            associated_tutors = Tutor.objects.filter(sign_languages=obj)
            if associated_tutors.exists():
                message = (
                    f"Cannot delete '{obj.name}' because it is associated "
                    "with tutors. Please remove this language from all "
                    "associated tutors before deleting it."
                )
                self.message_user(request, message, level=messages.ERROR)
                return False  # Prevent deletion and show the custom message

        return super().has_delete_permission(request, obj)


@admin.register(DayAvailability)
class DayAvailabilityAdmin(admin.ModelAdmin):
    """
    Admin configuration for the DayAvailability model.

    This manages the list of predefined days when a tutor can be
    available. The list of days is fixed and cannot be modified by
    the admin user.

    Attributes:
        list_display (tuple): Displays the name of the day.
        search_fields (tuple): Allows searching for a specific day by name.

    Methods:
        get_queryset: Limits the list to predefined days (Monday to Sunday).
        has_add_permission: Prevents adding new day entries.
        has_delete_permission: Prevents deletion of predefined days.
        has_change_permission: Prevents modification of existing days.
    """

    list_display = ('name',)

    def get_queryset(self, request):
        """Limits queryset to predefined days of the week."""
        return super().get_queryset(request).filter(name__in=[
            'Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday'
        ])

    def has_add_permission(self, request):
        """Prevent adding new day entries."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of predefined days."""
        return False

    def has_change_permission(self, request, obj=None):
        """Prevent modification of existing days."""
        return False


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TimeSlot model.

    This controls the management of time slots available for tutors. It
    prevents deletion of time slots that are associated with tutors.

    Attributes:
        list_display (tuple): Displays formatted start and
        end times for each time slot.
        search_fields (tuple): Allows searching by start and end times.

    Methods:
        formatted_start_time: Returns formatted start time as HH:MM.
        formatted_end_time: Returns formatted end time as HH:MM.

    Raises:
        messages.ERROR: If a time slot is in use by
        any tutor during deletion attempts.
    """

    list_display = ('formatted_start_time', 'formatted_end_time')
    search_fields = ('start_time', 'end_time')

    def formatted_start_time(self, obj):
        """Returns the start time formatted as HH:MM."""
        return obj.start_time.strftime('%H:%M')  # Returns as 24-hour format

    formatted_start_time.short_description = 'Start Time'

    def formatted_end_time(self, obj):
        """Returns the end time formatted as HH:MM."""
        return obj.end_time.strftime('%H:%M')  # Returns as 24-hour format

    formatted_end_time.short_description = 'End Time'

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of time slots that are associated with tutors.

        Args:
            request (HttpRequest): The HTTP request object.
            obj (Optional[TimeSlot]): The instance being deleted.

        Returns:
            bool: False if a time slot is in use by any tutor; otherwise True.
        """
        if obj:
            associated_tutors = Tutor.objects.filter(time_availability=obj)
            if associated_tutors.exists():
                message = (
                    f"Cannot delete '{obj.start_time.strftime('%H:%M')} - "
                    f"{obj.end_time.strftime('%H:%M')}' because it is \
                    associated with tutors. Please remove this time slot \
                    from all associated tutors before deleting it."
                )
                self.message_user(request, message, level=messages.ERROR)
                return False  # Prevent deletion and show custom message

        return super().has_delete_permission(request, obj)
