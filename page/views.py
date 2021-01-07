from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
# TODO: 각각의 view가 어떤 걸 의미하는지 Docstring으로 적어주세요.


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})


def new(request):
    return render(request, 'new.html')


def create(request):
    if request.method == 'POST':
        post = Post()
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.title = request.POST['title']
        post.text = request.POST['text']

        post.save()

        return redirect('detail', post.id)


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.title = request.POST['title']
        post.text = request.POST['text']

        post.save()
        return redirect('detail', post.id)
    else:
        return render(request, 'update.html', {'post': post})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')
