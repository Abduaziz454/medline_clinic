from django.contrib import admin
from .models import Blog, Category
from auth_app.models import Appointment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    list_display_links = ("name", )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "image", "time_create", "is_published")
    list_display_links = ("title", )
    list_editable = ("is_published", "image")
    list_filter = ("time_create", "is_published")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("pk", )
