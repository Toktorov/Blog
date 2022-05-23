from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "post_image/")