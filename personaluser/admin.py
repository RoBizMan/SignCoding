from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('personal_details', 'personal_firstname', 'personal_lastname')
    search_fields = ('personal_details__username', 'personal_firstname', 'personal_lastname')

admin.site.register(Profile, ProfileAdmin)