from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Tag
from .forms import PostForm, CommentForm


# render posts to landing page
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/index.html', {'posts': posts, 'title': 'index'})


# get a post by pk
def post(request, pk=None):
    item = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'item': item, 'title': item, })


# get a tag by pk
def tag(request, pk=None):
    _tag = get_object_or_404(Tag, pk=pk)
    posts = Post.objects.filter(tags__pk=pk)
    title = "Items tagged with {}".format(_tag)
    return render(request, 'base/tag.html', {'posts': posts, 'tag': _tag, 'title': title})


# create a post
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            form.save_m2m()
            return redirect(item.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'add_post', })


# edit a post
@login_required
def edit_post(request, pk=None):
    item = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(item.get_absolute_url())
    else:
        form = PostForm(instance=item)
        title = "Edit: {}".format(item)
        return render(request, 'blog/post_form.html', {'form': form, 'item': item, 'title': title, })


# create a comment to a post
def add_comment_to_post(request, pk=None):
    item = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = item
            comment.save()
            return redirect(item.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'form': form, 'item': item, })
