from django.contrib import admin

# Register your models here.
from .models import Building, Cond, Land


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ("city", "town", "street", "area")


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "town",
        "street",
        "area",
    )


@admin.register(Cond)
class CondAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "town",
        "street",
        "area",
    )
