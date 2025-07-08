
from django.urls import path
from django.http import HttpResponse

app_name = 'payments'

urlpatterns = [
    path('', lambda request: HttpResponse('<h1>مرحبًا بك في تطبيق المدفوعات</h1>'), name='home'),
]
