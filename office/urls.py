from django.urls import path
from . import views

app_name = 'office'

urlpatterns = [
    path('login/', views.office_login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.office_logout_view, name='logout'),
]
