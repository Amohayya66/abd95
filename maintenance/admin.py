from django.contrib import admin
from .models import MaintenanceRequest

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('unit', 'status', 'request_date')
    list_filter = ('status', 'request_date')
    search_fields = ('unit__number',)
