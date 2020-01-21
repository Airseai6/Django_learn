from django.urls import path, re_path
from app02 import views

urlpatterns = [
    re_path(r'^comment.html$', views.comment,),
    re_path(r'^test.html$', views.test,),
    re_path(r'^csrf1.html$', views.csrf1,),
    re_path(r'^login.html$', views.login,),
    re_path(r'^index.html$', views.index,),
]
