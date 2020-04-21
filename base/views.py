from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import RequestContext

# Create your views here.


def index(request):
    items = Post.objects.all()
    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'base/index.html', {'items': items, 'title': 'Home'})


def tag(request, pk=None):
    _tag = get_object_or_404(Tag, pk=pk)
    items = Post.objects.filter(tags__pk=pk)
    title = 'Items tagged with "{}"'.format(_tag)
    return render(request, 'base/tag.html', {'items': items, 'tag': _tag, 'title': title, })


class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def profile(request):
    return render(request, 'base/profile.html', {'title': 'profile'})


