from django.db import models
from residents.models import Resident

class Payment(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='payments', verbose_name="الساكن")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    payment_date = models.DateField(verbose_name="تاريخ الدفع")
    is_paid = models.BooleanField(default=True, verbose_name="تم الدفع؟")

    def __str__(self):
        return f"{self.resident.full_name} - {self.amount} ريال"
