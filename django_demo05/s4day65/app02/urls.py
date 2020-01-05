# -*- coding:utf-8 -*-
# @CreateTime : 2020/1/5 16:00
# @Author     : Qi

from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.classes),
    path('classes/', views.classes),
]
