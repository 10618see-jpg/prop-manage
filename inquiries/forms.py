from django import forms

from .models import Inquiry


# InquiryForm
class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "target_customer",
            "target_property",
            "inquiry_type",
            "inquiry_text",
        ]
