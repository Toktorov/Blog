from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    tel = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = "profile_image/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username