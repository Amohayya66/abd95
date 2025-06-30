from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OfficeStaff

@login_required(login_url='office:login')
def dashboard_view(request):
    try:
        # التحقق أن المستخدم هو موظف مكتب
        staff = OfficeStaff.objects.get(user=request.user)
    except OfficeStaff.DoesNotExist:
        return render(request, 'office/unauthorized.html', status=403)

    return render(request, 'office/dashboard.html', {'staff': staff})
