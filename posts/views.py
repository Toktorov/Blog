from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'index.html', context)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    context = {
        'post' : post
    }
    return render(request, 'blog_detail.html', context)