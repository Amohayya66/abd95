
from django.urls import path
from django.http import HttpResponse

app_name = 'complexes'

urlpatterns = [
    path('', lambda request: HttpResponse('<h1>مرحبًا بك في تطبيق المجمعات</h1>'), name='home'),
]
