from django.urls import path, re_path
from app02 import views

urlpatterns = [
    re_path(r'^comment.html$', views.comment,),
]
