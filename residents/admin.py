from django.contrib import admin
from .models import Resident

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'national_id', 'phone', 'unit', 'contract_start', 'contract_end')
    list_filter = ('contract_start', 'contract_end')
    search_fields = ('full_name', 'national_id', 'phone')
