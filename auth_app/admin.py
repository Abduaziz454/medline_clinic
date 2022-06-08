from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.Users)
class UsersAdmin(UserAdmin):
    list_display = ("pk", "username", "user_type", "first_name", "last_name", "email")
    list_display_links = ("username", )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'user_type', "phone", "country", "city", "address", "image")}),
    )


