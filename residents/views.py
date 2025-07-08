
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def resident_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # عدل المسار حسب الحاجة
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')

    return render(request, 'residents/login.html')
