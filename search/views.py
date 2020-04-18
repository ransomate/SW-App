from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post
from . import search

# Create your views here.


def search_blog(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        items = Post.objects.all()
    elif q is not None:
        items = search_blog(q)
        paginator = Paginator(items, 3)
        page = request.GET.get('page')
        items = paginator.get_page(page)
    title = "Search"
    return render(request, 'search/search.html', {'items':items,'title':title})


'''
def search_blog(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        items = Post.objects.all()
    elif q is not None:
        # Call post search
        items = search.post(q)
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    try:
    items = paginator.get_page(page)
    except EmptyPage:
    title = "Search"
    return render(request, 'search/search.html', {'items': items, 'title': title, })
'''