from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        date_of_birth = request.POST.get('date_of_birth')
        tel = request.POST.get('tel')
        profile_image = request.FILES.get('profile_image')
        image = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(image)
        if password1 == password2:
            try:
                user = User.objects.create(username=username, first_name = first_name, last_name = last_name, date_of_birth = date_of_birth, tel = tel, profile_image = profile_image)
                user.set_password(password1)
                user.save()
                return redirect('index')
            except:
                messages.error(request, 'Not correct some value')
        else:
            messages.error(request, 'Not correct password')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        except:
            messages.error("Неправильный логин или пароль")
       
    return render(request, 'login.html')
