from django.shortcuts import render
from .models import Post, Tag, Advert, PostLike
from django.contrib.auth.models import AbstractUser

# Create your views here.
def index(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    adverts = Advert.objects.all()
    context = {
        'posts' : posts,
        'tags' : tags,
        'adverts' : adverts,
    }
    return render(request, 'index.html', context)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        if 'like' in request.POST:
            try:
                like = PostLike.objects.get(user=request.user, post = post)
                like.delete()
            except:
                PostLike.objects.create(user = request.user, post = post)
    context = {
        'post' : post
    }
    return render(request, 'blog_detail.html', context)