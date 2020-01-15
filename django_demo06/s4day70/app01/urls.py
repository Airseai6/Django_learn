from django.urls import path, re_path
from app01 import views

urlpatterns = [
    # path(r'index/', views.index, name='n1'),
    # re_path(r'^edit/(\w+)/', views.edit, name='n2'),
    re_path(r'^index.html$', views.index,),
    re_path(r'^login.html$', views.Login.as_view()),
]
