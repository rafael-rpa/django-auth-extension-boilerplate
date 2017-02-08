from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]
    list_display = ['username', 'get_full_name', 'get_country', 'format_date_joined', 'format_last_login', 'is_staff']
    search_fields = ['username', 'full_name']
    list_filter = ['profile__country', 'is_staff']

    def get_full_name(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)
    get_full_name.short_description = 'Full name'

    def format_date_joined(self, obj):
        return obj.date_joined.strftime("%d/%m/%y - %H:%M")
    format_date_joined.short_description = 'Date (joined)'

    def format_last_login(self, obj):
        if obj.last_login:
            return obj.last_login.strftime("%d/%m/%y - %H:%M")
    format_last_login.short_description = 'Date (last login)'

    def get_country(self, instance):
        return instance.profile.country
    get_country.short_description = 'Country'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
