from django.db import models
from django.contrib.auth.models import User

class OfficeStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="حساب المستخدم")
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    phone = models.CharField(max_length=15, verbose_name="رقم الجوال")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    def __str__(self):
        return self.full_name
