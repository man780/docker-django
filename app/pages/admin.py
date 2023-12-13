from django.contrib import admin
from .models import Menu, Page


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "sequence", "title", "slug", "menu_id", "status",
        "created_time"
    )
    search_fields = ("title", "slug")
    list_filter = ("menu_id", "status")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "menu_id", "status",
        "created_time", "updated_time"
    )
    search_fields = ("title", "slug")
    list_filter = ("menu_id", "status")
