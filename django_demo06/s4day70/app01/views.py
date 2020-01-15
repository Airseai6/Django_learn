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
    models.UserType.objects.create(title='普通用户')
    models.UserType.objects.create(title='装逼用户')
    models.UserType.objects.create(title='大咖用户')

    return HttpResponse('...')


class PageInfo(object):

    def __init__(self, current_page, all_count, per_page, show_page=11):
        """
        """
        try:
            self.current_page = int(current_page)
        except Exception as e:
            print(e)
            self.current_page = 1
        self.per_page = per_page

        a, b = divmod(all_count, per_page)
        if b:
            a += 1
        self.all_pager = a
        self.show_page = show_page

    def start(self):
        return (self.current_page - 1)*self.per_page

    def end(self):
        return self.current_page*self.per_page

    def pager(self):
        # v = "<a href='/custom.html?page=1'>1</a>""<a href='/custom.html?page=2'>2</a>"
        # return v
        page_list = []


        if self.all_pager < self.show_page:
            begin = 1
            stop = self.all_pager+1
        else:
            half = int((self.show_page-1)/2)
            if self.current_page <= half:
                begin = 1
                stop = self.show_page+1
            elif self.current_page >= self.all_pager - half:
                begin = self.all_pager - self.show_page + 1
                stop = self.all_pager+1
            else:
                begin = self.current_page - half
                stop = self.current_page + half + 1


        if self.current_page > 1:
            prev = "<a style='display:inline-block; padding:5px; margin:5px;' href='/custom.html?page=%s'>上一页</a>" % (self.current_page - 1,)
            page_list.append(prev)

        for i in range(begin, stop):
            if i == self.current_page:
                temp = "<a style='display:inline-block; padding:5px; margin:5px; background-color:red;' href='/custom.html?page=%s'>%s</a>" %(i, i)
            else:
                temp = "<a style='display:inline-block; padding:5px; margin:5px;' href='/custom.html?page=%s'>%s</a>" %(i, i)

            page_list.append(temp)
        
        if self.current_page < self.all_pager:
            nextpage = "<a style='display:inline-block; padding:5px; margin:5px;' href='/custom.html?page=%s'>下一页</a>" % (self.current_page + 1,)
            page_list.append(nextpage)
        
        return ''.join(page_list)



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

    page_info = PageInfo(request.GET.get('page'), all_count, 10)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]

    return render(request, 'custom.html', {'user_list': user_list, 'page_info':page_info,})
