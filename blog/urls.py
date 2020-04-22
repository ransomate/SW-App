from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.post, name='item'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('add/post/', views.add_post, name='add_post'),
    path('edit/post/<int:pk>/', views.edit_post, name='edit_post'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='comment'),
]