from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpRequest

# === العروض البسيطة لعرض القوالب مباشرة ===

def home_view(request: HttpRequest):
    return render(request, 'home.html')

def admin_login_view(request: HttpRequest):
    return render(request, 'admin_login.html')

def resident_login_view(request: HttpRequest):
    return render(request, 'resident_login.html')

# === روابط المشروع ===

urlpatterns = [
    # لوحة تحكم Django
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', home_view, name='home'),

    # صفحات الدخول المخصصة
    path('admin-login/', admin_login_view, name='admin_login'),
    path('resident-login/', resident_login_view, name='resident_login'),

    # روابط التطبيقات الداخلية
    path('complexes/', include('complexes.urls')),
    path('units/', include('units.urls')),
    path('residents/', include('residents.urls')),
    path('payments/', include('payments.urls')),
    path('maintenance/', include('maintenance.urls')),
]
