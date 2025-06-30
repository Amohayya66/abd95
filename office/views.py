from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OfficeLoginForm, OfficeStaffCreationForm

def office_login_view(request):
    if request.method == 'POST':
        form = OfficeLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect('office:dashboard')
            else:
                form.add_error(None, 'ليس لديك صلاحية الدخول كموظف مكتب.')
    else:
        form = OfficeLoginForm()
    return render(request, 'office/login.html', {'form': form})

@login_required(login_url='office:login')
def dashboard_view(request):
    return render(request, 'office/dashboard.html')

def office_logout_view(request):
    logout(request)
    return redirect('office:login')

@staff_member_required(login_url='admin:login')
def create_office_staff_view(request):
    if request.method == 'POST':
        form = OfficeStaffCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office:dashboard')
    else:
        form = OfficeStaffCreationForm()
    return render(request, 'office/create_staff.html', {'form': form})
