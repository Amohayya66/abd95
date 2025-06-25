from django.db import models
from units.models import Unit

class Resident(models.Model):
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, verbose_name="الوحدة")
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    national_id = models.CharField(max_length=20, unique=True, verbose_name="رقم الهوية")
    phone = models.CharField(max_length=15, verbose_name="رقم الجوال")
    contract_start = models.DateField(verbose_name="تاريخ بداية العقد")
    contract_end = models.DateField(verbose_name="تاريخ نهاية العقد")

    def __str__(self):
        return self.full_name
