from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app02 import models

# Create your views here.
msg = []


def comment(request):
    if request.method == 'GET':
        return render(request, 'comment.html')
    else:
        v = request.POST.get('content')
        msg.append(v)
        return render(request, 'comment.html', {'msg':msg})


def test(request):
    print('------------------ ORM 练习测试区域 start ------------------')
    # 多对多
    # objs = [
    #     models.Boy(name='方少伟'),
    #     models.Boy(name='由秦兵'),
    #     models.Boy(name='陈涛'),
    #     models.Boy(name='闫龙'),
    #     models.Boy(name='吴彦祖'),
    # ]
    # models.Boy.objects.bulk_create(objs, 5)

    # objs2 = [
    #     models.Girl(nick='小雨'),
    #     models.Girl(nick='小周'),
    #     models.Girl(nick='小猫'),
    #     models.Girl(nick='小狗'),
    # ]
    # models.Girl.objects.bulk_create(objs2, 5)

    # models.Love.objects.create(b_id=1, g_id=1)
    # models.Love.objects.create(b_id=1, g_id=4)
    # models.Love.objects.create(b_id=2, g_id=4)
    # models.Love.objects.create(b_id=2, g_id=2)

    # 1、和方少伟有关系的姑娘
    obj = models.Boy.objects.filter(name='方少伟').first()
    love_list = obj.love_set.all()
    for row in love_list:
        print(row.g.nick)

    love_list = models.Love.objects.filter(b__name='方少伟')
    for row in love_list:
        print(row.g.nick)

    # 上述两种方法循环中会连表，采用只连一次表，循环中不连表的方式
    love_list = models.Love.objects.filter(b__name='方少伟').values('g__nick')
    for item in love_list:
        print(item['g__nick'])

    love_list = models.Love.objects.filter(b__name='方少伟').select_related('g')
    for obj in love_list:
        print(obj.g.nick)


    print('------------------ ORM 练习测试区域  end ------------------')
    return HttpResponse('...')


def csrf1(request):
    if request.method == 'GET':
        return render(request, '/anl/csrf1.html')
    else:
        return HttpResponse('ok')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserAdmin.objects.filter(username=u, password=p).first()
        if obj:
            # 1、生成随机字符串
            # 2、通过cookie发送个客户端
            # 3、服务器保存
            # {
            #     随机字符串1: [username:'xxx', password:'xxx', ....]
            # }
            request.session['username'] = obj.username
            return redirect('/app02/index.html')
        else:
            return render(request, 'login.html', {'msg':'用户或密码错误'})


def index(request):
    v = request.session.get('username')
    if v:
        return HttpResponse('login success %s' %v)
    else:
        return redirect('/app02/login.html')