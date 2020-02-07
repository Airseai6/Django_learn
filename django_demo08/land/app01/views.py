from django.forms import Form, fields
from django.shortcuts import render, HttpResponse, redirect

from . import models
from utils.pager import PageInfo
from django.http import FileResponse
import json, time


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


# def refresh(request):
#     dataRet = models.get_data()
#     return HttpResponse('ok')


def index(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        dataRet = models.get_data()
        # print('index有进来重新加载了一次')
        return render(request, 'index.html', {'username': username, 'dataRet': dataRet},)
    else:
        return redirect('/login/')


def charts(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        dataRet = models.get_data()
        # print('charts有进来重新加载了一次')
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

from django.utils.http import urlquote
def download(request):
    username = request.get_signed_cookie('username', default=0, salt='123')
    if username:
        try:
            if request.POST.get('dtype') == '1':
                dataRet = models.get_data()
                data = json.dumps(dataRet, ensure_ascii=False)
                filename = '2019-nCoV疫情数据_' + str(time.strftime("%Y-%m-%d", time.localtime())) + '.json'
            else:
                data = json.dumps(newsRet, ensure_ascii=False)
                filename = '2019-nCoV疫情新闻_' + str(time.strftime("%Y-%m-%d", time.localtime())) + '.json'
            
            response = FileResponse(data)
            response['Content-Type']='application/octet-stream'  
            response['Content-Disposition']='attachment;filename="{}"'.format(urlquote(filename))
            return response
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect('/login/')
    