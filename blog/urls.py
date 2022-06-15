"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import index, post_detail, post_create, post_update, post_delete
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from users.views import register, user_login, profile, update_profile, delete_profile


urlpatterns = [
    path('', index, name = "index"),
    path('post/<int:id>', post_detail, name = "post_detail"),
    path('post/create', post_create, name = "post_create"),
    path('post/update/<int:id>', post_update, name = "post_update"),
    path('post/delete/<int:id>', post_delete, name = "post_delete"),
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('user/<int:id>', profile, name = "profile"),
    path('user/update/<int:id>', update_profile, name = "update_profile"),
    path('user/delete/<int:id>', delete_profile, name = "delete_profile"),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = "logout"),
    path('admin/', admin.site.urls),
]
#http://127.0.0.1:8000/user/2
#http://127.0.0.1:8000/post/update/5
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)