from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path(r'index/', views.index, name='n1'),
    re_path(r'^edit/(\w+)/', views.edit, name='n2'),
    # path('edit/<slug:slug>/', views.edit),
    # re_path(r'^edit/(?P<a1>\w+)/(?P<a2>\w+)/', views.edit),
]
