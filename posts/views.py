from itertools import product
from django.shortcuts import redirect, render
from .models import Post, Tag, Advert, PostLike, PostComment, Alert
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    adverts = Advert.objects.all()
    alert = Alert.objects.latest('id')
    context = {
        'posts' : posts,
        'tags' : tags,
        'adverts' : adverts,
        'alert' : alert,
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

def post_update(request, id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Post.objects.get(id = id)
        post.title = title 
        post.description = description 
        post.image = image 
        post.save()
        return redirect('post_detail', post.id)
        # http://127.0.0.1:8000/post/update/1
        
    context = {
        'post' : post,
    }
    return render(request, 'post_update.html', context)

def post_delete(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('index')
    return render(request, 'post_delete.html')

def post_search(request):
    posts = Post.objects.all()
    qury_obj = request.GET.get('key')
    if qury_obj:
        posts = Post.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'posts' : posts
    }
    return render(request, 'post_search.html', context)