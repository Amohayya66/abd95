from django.urls import path
from django.http import HttpResponse

# عرض مؤقت للصفحة الرئيسية لتطبيق المجمعات السكنية
def placeholder_view(request):
    return HttpResponse("<h1 style='text-align:center; margin-top:50px;'>مرحبًا بك في تطبيق إدارة المجمعات السكنية</h1>")

app_name = 'complexes'

urlpatterns = [
    path('', placeholder_view, name='home'),
]
