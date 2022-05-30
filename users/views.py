from django.shortcuts import render, redirect
from users.models import Profile
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def signup(request):
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
                user = User.objects.create(username = username)
                user.set_password(password1)
                user.save()
                profile = Profile.objects.create(user = user, username = username, first_name = first_name, last_name = last_name, date_of_birth = date_of_birth, tel = tel, profile_image = profile_image)
                user = authenticate(username = username, pasword = password1)
                login(request, user)
                return redirect('index')
            except:
                messages.error(request, "Неправильные данные")
        else:
            messages.error(request, 'Пароли отличаются')
    return render(request, 'register.html')