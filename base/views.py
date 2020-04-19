from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag

# Create your views here.


def index(request):
    items = Post.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'base/index.html', {'items': items, 'title': 'Home'})


def tag(request, slug=None):
    _tag = get_object_or_404(Tag, slug=slug)
    items = Post.objects.filter(tags__slug=slug)
    title = 'Items tagged with "{}"'.format(_tag)
    return render(request, 'base/tag.html', {'items': items, 'tag': _tag, 'title': title, })

