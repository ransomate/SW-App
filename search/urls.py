from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_blog, name='search'),
    path('search', views.search_blog, name='search'),
]