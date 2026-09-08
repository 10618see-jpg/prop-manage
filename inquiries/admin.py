from django.contrib import admin

from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        "target_customer",
        "target_property",
        "get_inquiry_type_display",
        "inquiry_text",
    )
