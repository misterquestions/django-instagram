from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('pk', 'user', 'phone_number', 'web_site', 'profile_picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'web_site', 'profile_picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number',
        'web_site'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'user__date_joined',
        'date_modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'profile_picture'),
            ),
        }),
        ('Extra info', {
            'fields': (
                ('web_site', 'phone_number'),
                'biography',
            ),
        }),
        ('Metadata', {
            'fields': (
                ('date_modified'),
            ),
        }),
    )

    readonly_fields = ('date_modified',)

class ProfileInline(admin.StackedInline):
    """
    Profile in-line admin for users.

    Helps creating profile at once, when adding a new user
    """

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)