
from django.urls import path
from . import views

app_name = 'residents'

urlpatterns = [
    path('login/', views.resident_login_view, name='login'),
]
