from django.shortcuts import render
from .models import Post, Tag, Advert

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
    context = {
        'post' : post
    }
    return render(request, 'blog_detail.html', context)