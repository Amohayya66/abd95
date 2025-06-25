from django.db import models

class Complex(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المجمع")
    location = models.TextField(verbose_name="الموقع")
    manager_name = models.CharField(max_length=100, verbose_name="اسم المدير")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
