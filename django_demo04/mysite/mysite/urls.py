"""mysite URL Configuration

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
from django.urls import path
from django.shortcuts import HttpResponse, render, redirect


def login(request):
    """
    deal user's request, and return content
    :param request:
    :return:
    """
    # HttpResponse only used to str not files
    # return HttpResponse('<input type="text"/>')
    # return HttpResponse('login.html')
    # print(request)
    # print(request.method)
    if request.method == "GET":
        return render(request, 'login.html', {'msg':'123'})
    else:
        # the data user submit
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u == 'root' and p =='123123':
            # TODO sucess
            # return redirect('http://www.oldboyedu.com')
            # return render(request, 'index.html')
            return redirect('/index/')
        else:
            # TODO fail
            return render(request, 'login.html', {'msg':'Failed'})


def index(request):
    # return HttpResponse('index')
    return render(
        request,
        'index.html',
        {
            'name':'Alex',
            'users':['xiaoming','zhanghua'],
            'user_dict':{'k1':'v1', 'k2':'v2'},
            'user_dict_list':[
                {'id':1, 'name':'alex', 'email':'alex@126.com'},
                {'id':2, 'name':'alex2', 'email':'alex2@126.com'},
                {'id':3, 'name':'alex3', 'email':'alex3@126.com'},
            ]
        }
    )


def delet(request):
    return HttpResponse(request.method + ' DELET ' + request.GET.get('nid'))


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login),
    path('login/', login),
    path('index/', index),
    path('del/', delet),
]
