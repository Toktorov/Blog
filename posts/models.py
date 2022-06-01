from distutils.command.upload import upload
from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "post_image/")

    def __str__(self):
        return self.title

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts_post")

class Tag(models.Model):
    title = models.CharField(max_length=100)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.title

class Advert(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    advert_image = models.ImageField(upload_to = 'advert_image/')
    url = models.URLField()

    def __str__(self):
        return self.title