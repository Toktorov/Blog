from email import message
import re
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from .models import Post, Tag, Advert, PostLike, PostComment
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
    comments = PostComment.objects.all()
    if request.method == "POST":
        if 'like' in request.POST:
            try:
                like = PostLike.objects.get(user=request.user, post = post)
                like.delete()
            except:
                PostLike.objects.create(user = request.user, post = post)
        if 'comment' in request.POST:
            try:
                text = request.POST.get('text')
                comment = PostComment.objects.create(user = request.user, post = post, text = text)
                return redirect('post_detail', post.id)
            except:
                return redirect('post_detail', post.id)
                
    context = {
        'post' : post,
        'comments' : comments,
    }
    return render(request, 'blog_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post_obj = Post.objects.create(user = request.user, title = title, description = description, image = image)
        return redirect('index')
    return render(request, 'post_create.html')