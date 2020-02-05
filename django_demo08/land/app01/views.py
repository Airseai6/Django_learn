from django.forms import Form, fields
from django.shortcuts import render, HttpResponse, redirect

from . import models
from utils.pager import PageInfo
from django.http import FileResponse


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


global newsRet
newsRet = models.get_news()[::-1]

def news(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        # newsRet = models.get_news()[::-1]
        dataRet = models.get_data()

        page_info = PageInfo(request.GET.get('page'), len(newsRet), 5, '/news',)
        news_list = newsRet[page_info.start():page_info.end()]

        return render(request, 'news.html', {'username': username, 'page_info': page_info, 'news_list': news_list, },)
    else:
        return redirect('/login/')


def download(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        try:
            file=open(r'E:\02_Scripts\Python\Django_learn\django_demo08\land\static\css\commons.css','rb')
            print(type(file))
            # response = FileResponse(file)
            response = FileResponse('123')
            response['Content-Type']='application/octet-stream'  
            response['Content-Disposition']='attachment;filename="test.txt"'  
            return response
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect('/login/')
    