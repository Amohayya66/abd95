
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# صفحة رئيسية مؤقتة

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('office/', include('office.urls', namespace='office')),
    path('residents/', include('residents.urls', namespace='residents')),
    path('complexes/', include('complexes.urls', namespace='complexes')),
    path('units/', include('units.urls', namespace='units')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('maintenance/', include('maintenance.urls', namespace='maintenance')),
]  
