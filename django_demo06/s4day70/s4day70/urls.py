"""s4day70 URL Configuration

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
from django.urls import path, re_path, include
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include('app01.urls')),
    path('anl/', include('app02.urls')),
    # path('index/', views.index),
    # re_path(r'^edit/(\w+)/(\w+)/', views.edit),
    # re_path(r'^edit/(?P<a1>\w+)/(?P<a2>\w+)/', views.edit),
    path('test/', views.test),
    re_path(r'^custom.html$', views.custom),
]
