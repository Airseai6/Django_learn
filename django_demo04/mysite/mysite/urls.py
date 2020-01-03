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
from django.shortcuts import HttpResponse, render


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
        return render(request, 'login.html')
    else:
        # the data user submit
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        if u == 'root' and p =='123123':
            # TODO sucess
            pass
        else:
            # TODO fail
            pass


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login),
]
