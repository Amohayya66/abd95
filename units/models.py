from django.db import models
from complexes.models import Complex

class Unit(models.Model):
    UNIT_TYPES = [
        ('apartment', 'شقة'),
        ('villa', 'فيلا'),
        ('studio', 'استوديو'),
    ]

    complex = models.ForeignKey(Complex, on_delete=models.CASCADE, related_name='units', verbose_name="المجمع")
    number = models.CharField(max_length=10, verbose_name="رقم الوحدة")
    floor = models.IntegerField(verbose_name="الطابق")
    area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="المساحة (م²)")
    unit_type = models.CharField(max_length=20, choices=UNIT_TYPES, verbose_name="نوع الوحدة")
    is_occupied = models.BooleanField(default=False, verbose_name="مشغولة؟")

    def __str__(self):
        return f"{self.number} - {self.complex.name}"
