from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


class InlineProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = [
        'user',
        ('avatar', 'avatar_image'),
        'interests'
    ]
    readonly_fields = ['avatar_image']

    def avatar_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" />'.format(
                url=obj.avatar.url,
                width=200
            )
        )


class CustomUserAdmin(UserAdmin):
    inlines = (InlineProfileAdmin,)
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'avatar_image']
    fieldsets = (
        (None, {'fields': (('username', 'email'), 'password')}),
        ('Personal info', {'fields': (('first_name', 'last_name'),),}),
        ('Permissions', {
            'fields': (('is_active', 'is_staff', 'is_superuser'), 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': (('last_login', 'date_joined'),)}),
    )
    readonly_fields = ['last_login', 'date_joined']

    def avatar_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" />'.format(
                url=obj.profile.avatar.url,
                width=60
            )
        )

    avatar_image.short_description = 'Avatar'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# admin.site.register(Profile)
