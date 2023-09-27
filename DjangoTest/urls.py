"""
URL configuration for DjangoTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from user import views as userApi

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', demo),
    # path('index2/', index),
    # path('myApp/', include('myApp.urls'))
    path('login/', userApi.login, name='login'),
    path('register/', userApi.register, name='register'),
    path('logout/', userApi.logout, name="logout"),
    path('myApp/', include(('myApp.urls', 'App'), namespace='App')),
    path('movie/', include(('movie.urls', 'Movie'), namespace='Movie'))
]

