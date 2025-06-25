from django.db import models
from units.models import Unit

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('in_progress', 'قيد التنفيذ'),
        ('done', 'تم الإنجاز'),
    ]

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='maintenance_requests', verbose_name="الوحدة")
    description = models.TextField(verbose_name="الوصف")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="الحالة")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    def __str__(self):
        return f"{self.unit} - {self.status}"
