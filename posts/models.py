from distutils.command.upload import upload
from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "post_user", null = True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "post_image/")

    def __str__(self):
        return self.title

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts_post")

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-created', )

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
        
class Alert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    alert_image = models.ImageField(upload_to = "alert_image/")

    def __str__(self):
        return self.title 