from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.post, name='item'),
    path('tags/<slug:slug>/', views.tag, name='tag'),
    path('add/post/', views.add_post, name='add_post'),
    path('edit/post/<int:pk>/', views.edit_post, name='edit_post'),
]