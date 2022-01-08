"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.registration import registration, sign_in
from blog.views import index, category, author, comments, create_ad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<int:pk>', category, name='category'),
    path('author/<int:pk>', author, name='author'),
    path('comments/<int:pk>', comments, name='comments'),
    path('login/', sign_in, name='login'),
    path('registration/', registration, name='reg'),
    path('create-ad/', create_ad, name='create_ad'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
