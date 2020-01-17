from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app01 import models

# def index(request):
#     user_list = [
#         'alex', 'eric', 'tony',
#     ]
#     v = reverse('n1')
#     print(v)
#     return render(request, 'index.html', {'user_list':user_list})


# def edit(request, a1):
#     print(a1)
#     return HttpResponse('...')


# ------------------ 数据库相关操作 ------------------
def index(request):
    # 增删改查
    from app01 import models

    # 新增
    # models.UserGroup.objects.create(title='销售部')
    # models.UserInfo.objects.create(username='root', password='pwd', age=18, ug_id=1)

    # 查找
    # group_list = models.UserGroup.objects.filter(id=1)
    # group_list = models.UserGroup.objects.filter(id__gt=1)
    # group_list = models.UserGroup.objects.filter(id__lt=1)
    # group_list是一个 QuerySet 类型（列表）
    # print(group_list)
    # for row in group_list:
    #     print(row.id, row.title)
    # models.UserInfo.objects.all()

    # 删除
    # models.UserGroup.objects.filter(id=2).delete()

    # 更新
    models.UserGroup.objects.filter(id=2).update(title='公关部')


    group_list = models.UserGroup.objects.filter(id=1)
    # return HttpResponse('...')
    return render(request, 'newindex.html', {"group_list": group_list})

from django.views import View
class Login(View):
    """
    get    查
    post   创建
    put    更新
    delete 删除
    """
    def get(self, request):
        
        return render(request, 'login.html')

    def post(self, request):
        # for i in range(300):
        #     root = 'root' + str(i)
        #     models.UserInfo.objects.create(username=root, password='pwd', age=18, ug_id=1)
        print(request.POST.get('user'))
        return HttpResponse('Login.post')


def test(request):
    # 创建数据
    # models.UserType.objects.create(title='普通用户')
    # models.UserType.objects.create(title='装逼用户')
    # models.UserType.objects.create(title='大咖用户')

    # models.UserInfo.objects.filter(nid__gt=8).delete()
    # models.UserInfo2.objects.create(
    #     name='alex', age=18, ut_id=1)
    # models.UserInfo2.objects.create(
    #     name='eric', age=18, ut_id=2)
    # models.UserInfo2.objects.create(
    #     name='zhihu', age=18, ut_id=3)

    # 排序
    # user_list = models.UserInfo2.objects.all().order_by('id')
    # user_list = models.UserInfo2.objects.all().order_by('-id', 'name')
    # print(user_list)

    # 分组
    # v = models.UserInfo2.objects.values('ut_id')     # select ut_id from userinfo
    # from django.db.models import Count
    # v = models.UserInfo2.objects.values('ut_id').annotate(xx=Count('id'))
    # print(v.query)
    # v = models.UserInfo2.objects.values('ut_id').annotate(xx=Count('id')).filter(xx__gt=2)
    # print(v.query)
    # v = models.UserInfo2.objects.filter(id__gt=2).values('ut_id').annotate(xx=Count('id')).filter(xx__gt=2)
    # print(v.query)

    # # select_related 查询主动做连表
    # q = models.UserInfo2.objects.all().select_related('ut')
    # # select * from userinfo
    # # select * from userinfo inner join usertype on ...
    # for row in q:
    #     print(row.name, row.ut.title)

    return HttpResponse('...')

from utils.pager import PageInfo
def custom(request):
    # # 表示用户当前想要访问的页码 8
    # current_page = request.GET.get('page')
    # current_page = int(current_page)
    # # 每页显示的数据的个数
    # per_page = 10

    # start = (current_page-1)*per_page
    # end = current_page*per_page

    # user_list = models.UserInfo.objects.all()[start: end]

    all_count = models.UserInfo.objects.all().count()

    page_info = PageInfo(request.GET.get('page'), all_count, 10, '/custom.html',)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]

    return render(request, 'custom.html', {'user_list': user_list, 'page_info':page_info,})
