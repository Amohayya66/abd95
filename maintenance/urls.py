
from django.urls import path
from django.http import HttpResponse

app_name = 'maintenance'

urlpatterns = [
    path('', lambda request: HttpResponse('<h1>مرحبًا بك في تطبيق الصيانة</h1>'), name='home'),
]
