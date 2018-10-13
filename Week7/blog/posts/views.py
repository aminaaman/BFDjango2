from django.shortcuts import render, redirect
from .forms import TitleForm, PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = TitleForm(request.GET or None)
        if form.is_valid():
            search = form.cleaned_data['title']

            context = {
                'posts': Post.objects.filter(title__contains=search),
                'form': form
            }

            return render(request, 'index.html', context)

        if request.GET.get('order', '') != '':
            context = {
                'posts': Post.objects.order_by('-published')
            }
            return render(request, 'index.html', context)

    form = TitleForm()
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'index.html', context)


def post_details(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
        'comments': post.comments.all(),
        'pk': pk,
    }
    return render(request, 'posts/post_details.html', context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/add_post.html', context)


@login_required
def add_comment(request, fk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            message = form.cleaned_data['message']
            post = Post.objects.get(pk=fk)
            comment = Comment()
            comment.user = user
            comment.message = message
            comment.post = post
            comment.save()
            return redirect('.')
    else:
        form = CommentForm()
    context = {
        'form': form,
        'users': User.objects.all(),
    }
    return render(request, 'posts/add_comment.html', context)


@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/')

@login_required
def delete_comment(request, fk, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('..')


