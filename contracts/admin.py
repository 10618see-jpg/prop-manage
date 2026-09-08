from django.contrib import admin

# Register your models here.
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display =(
        'target_property',
        'target_customer',
        'target_accounts',
        'contract_price',
        'contract_date',
        'handover_date',
        'get_status_display',
    )