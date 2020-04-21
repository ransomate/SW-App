"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from base import views
from . import settings


urlpatterns = [
    path('', include('base.urls')),
    path('blog/', include('blog.urls')),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('search/', include('search.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', views.Register.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/profile', views.profile, name='profile')
# not worked with these urls below
#    path('accounts/register/', views.Register.as_view(), name='register'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('account/', include('account.urls')),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('dashboard/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
