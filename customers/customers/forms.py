from django import forms

from .models import Customer

# customer_create_form
class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address', 'free_text']