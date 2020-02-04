from django.forms import Form, fields
from django.shortcuts import render, HttpResponse, redirect

from . import models


class LoginFrom(Form):
    username = fields.CharField(max_length=18, required=True)
    password = fields.CharField(max_length=16, required=True)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        obj = LoginFrom(request.POST)
        if obj.is_valid():
            # if obj.cleaned_data['username'] == 'root' and obj.cleaned_data['password'] == '123':
            #     ret = redirect('/index/')
            #     ret.set_signed_cookie('username', obj.cleaned_data['username'], salt='123')
            #     return ret
            # else:
            #     msg_err = 'Incorrect user name or password.'
            #     return render(request, 'login.html', {'msg_err': msg_err})
            ret = redirect('/index/')
            ret.set_signed_cookie('username', obj.cleaned_data['username'], salt='123')
            return ret
        else:
            return render(request, 'login.html', {'obj': obj})


def logout(request):
    rep = redirect("/login/")
    rep.delete_cookie("username")
    return rep


# global dataRet
# dataRet = models.get_data()
# dataRet.pop('isShowAdd')


# def refresh(request):
#     dataRet = models.get_data()
#     dataRet.pop('isShowAdd')
#     return HttpResponse('ok')


def index(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        dataRet = models.get_data()
        dataRet.pop('isShowAdd')
        return render(request, 'index.html', {'username': username, 'dataRet': dataRet},)
    else:
        return redirect('/login/')


def charts(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        dataRet = models.get_data()
        dataRet.pop('isShowAdd')
        return render(request, 'charts.html', {'username': username, 'dataRet': dataRet},)
    else:
        return redirect('/login/')
