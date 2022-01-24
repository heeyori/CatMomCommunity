"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from miniapp import views as miniapp_views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', miniapp_views.login),
    path('signup/', miniapp_views.signup),
    path('create_cat/', miniapp_views.create_cat),
    path('signup_complete/', miniapp_views.signup_complete),
    path('login_complete/', miniapp_views.login_complete),
    path('upload_cat_img/',miniapp_views.upload_cat_img),
    path('show/', miniapp_views.show),
    path('my_cat/', miniapp_views.my_cat),
]
