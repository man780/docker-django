from django.contrib import admin
from .models import Menu, Page


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "sequence", "title", "slug", "menu_id", "status", "place",
        "created_time", "updated_time", "created_user", "updated_user",
    )
    search_fields = ("title", "slug")
    list_filter = ("menu_id", "status")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "menu_id", "status", "author", "publish_date",
        "created_time", "updated_time", "created_user", "updated_user",
    )
    search_fields = ("title", "slug")
    list_filter = ("menu_id", "status")
