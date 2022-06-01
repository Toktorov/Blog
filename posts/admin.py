from django.contrib import admin
from .models import Post, Tag, Advert, PostLike

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Advert)
admin.site.register(PostLike)