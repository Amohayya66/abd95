from django.contrib import admin
from .models import Complex

@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'manager_name', 'created_at')
    search_fields = ('name', 'manager_name')
    list_filter = ('created_at',)
