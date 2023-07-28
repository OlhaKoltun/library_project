from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from .models import CustomUser


def users_list_view(request):
    context = {'users': CustomUser.objects.all()}

    return render(request, 'users_list.html', context)


def user_detail_view(request, id=None):
    user_object = None

    if id:
        user_object = CustomUser.objects.get(pk=id)
    context = {'user': user_object}

    return render(request, 'user_detail.html', context=context)


def register_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        role = request.POST.get('role')

        user_object = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
                                                     last_name=last_name, middle_name=middle_name, role=role)
        context['object'] = user_object
        context['created'] = True

    return render(request, 'register.html', context=context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser.objects.get(email=email)

        if user is None:
            context = {"error": "No User Exist"}
            return render(request, 'login.html', context)

        if not user.check_password(password):
            context = {"error": "Incorrect Password"}
            return render(request, 'login.html', context)

        login(request, user)
        user.update(is_active=True)
        return redirect('/')

    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    
    return render(request, 'logout.html', {})
