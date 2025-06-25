from django.contrib import admin
from .models import Unit

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('number', 'complex', 'floor', 'area', 'unit_type', 'is_occupied')
    list_filter = ('complex', 'unit_type', 'is_occupied')
    search_fields = ('number',)
