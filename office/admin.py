from django.contrib import admin
from .models import OfficeStaff

@admin.register(OfficeStaff)
class OfficeStaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'phone', 'is_active', 'created_at')
    search_fields = ('full_name', 'user__username')
    list_filter = ('is_active',)
