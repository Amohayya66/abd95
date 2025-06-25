from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('resident', 'amount', 'payment_date', 'is_paid')
    list_filter = ('payment_date', 'is_paid')
    search_fields = ('resident__full_name',)
