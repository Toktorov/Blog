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
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create(username=username, first_name = first_name, last_name = last_name, date_of_birth = date_of_birth, tel = tel, profile_image = profile_image)
                user.set_password(password1)
                user.save()
                return redirect('index')
            except:
                messages.error(request, 'Неправильные данные')
        else:
            messages.error(request, 'Пароли отличаются')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error("Неправильный логин или пароль")
       
    return render(request, 'login.html')

def profile(request, id):
    user = User.objects.get(id = id)
    context = {
        'user' : user, 
    }
    return render(request, 'profile.html', context)

def update_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        tel = request.POST.get('tel')
        date_of_birth = request.POST.get('date_of_birth')
        user = User.objects.get(id = id)
        user.username = username 
        user.fist_name = first_name
        user.last_name = last_name
        user.tel = tel 
        user.date_of_birth = date_of_birth
        user.save()
        return redirect('profile', user.id)
    context = {
        'user' : user,
    }
    return render(request, 'profile_update.html', context)

def delete_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user = User.objects.get(id = id)
        user.delete()
        return redirect('index')
    context = {
        'user' : user
    }
    return render(request, 'profile_delete.html', context)