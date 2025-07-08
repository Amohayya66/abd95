
from django.urls import path
from django.http import HttpResponse

app_name = 'units'

urlpatterns = [
    path('', lambda request: HttpResponse('<h1>مرحبًا بك في تطبيق الوحدات</h1>'), name='home'),
]
