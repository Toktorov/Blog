from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank = True)
    tel = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = "profile_image/")

    def __str__(self):
        return self.username