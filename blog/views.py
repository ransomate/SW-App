from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Tag
from .forms import PostForm


# Create your views here.

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/index.html', {'posts': posts, 'title': 'index'})


def post(request, slug=None):
    item = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'item': item, 'title': item, })


def tag(request, slug=None):
    _tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__slug=slug)
    title = "Items tagged with {}".format(_tag)
    return render(request, 'base/tag.html', {'posts': posts, 'tag': _tag, 'title': title})


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return redirect(item.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'add_post', })


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
