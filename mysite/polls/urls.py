# -*- coding:utf-8 -*-
# @Time   : 2019/12/28 22:54
# @Author : Qi

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
