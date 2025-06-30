from django.urls import path
from .views import office_login_view, dashboard_view, office_logout_view, create_office_staff_view

app_name = 'office'

urlpatterns = [
    path('login/', office_login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', office_logout_view, name='logout'),
    path('create-staff/', create_office_staff_view, name='create_staff'),
]
