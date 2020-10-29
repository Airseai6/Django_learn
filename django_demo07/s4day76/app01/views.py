from django.forms import Form, fields
from django.shortcuts import render, HttpResponse
from app01 import models


def test(request):
    print('test')

    # from MDSplus import Tree
    # tree = Tree('exl50_copy', 4118)

    # shotTime = tree.getNode('AI:' + 'G1_IK_F').getTimeInserted().date
    # data = str(list(tree.getNode('AI:' + 'G1_IK_F').data()))

    # models.tempChannelData.objects.create(
    #     shot_channel = '4118_M1_PIN',
    #     shot = '4118',
    #     channel = 'M1_PIN',
    #     isHaveData = True,
    #     xAis = {"len":5002,"start":-5.0,"end":10.003},
    #     yAis = data,
    #     yInfo = {"min":5002,"max":-5.0,"unit":"kA"},
    #     shotTime = shotTime,
    # )

    data = models.tempChannelData.objects.filter(nid=5)
    print(type(data[0].yAis))
    # print(data[0].yAis)
    print(len(data[0].yAis))
    temp = data[0].yAis[1:-1].split(', ')
    print(len(temp))
    print(temp[0])
    print(temp[111])
    print(temp[222])
    print(temp[-1])


    return HttpResponse('execute views')


class LoginFrom(Form):
    # 正则的验证
    username = fields.CharField(max_length=18, required=True)
    # 正则的验证
    password = fields.CharField(max_length=16, required=True)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # user = request.POST.get('username')
        # pwd = request.POST.get('password')
        # if user == 'root' and pwd == '123':
        #     return HttpResponse('ok')
        # else:
        #     return render(request, 'login.html', {'msg': 'username or pwd is error !'})
        obj = LoginFrom(request.POST)
        """
        1. LoginForm实例化时
             self.fields={
                 'username':正则表达式，
                 'password':正则表达式，
             }
        2. 循环self.fields
            for k, v in self.fields.items():
                k是：username，password
                v是：正则表达式
                input_value = request.POST.get(k)
        """
        if obj.is_valid():
            print('****************')
            print(obj.cleaned_data) # 字典类型
            print('****************')
            # .create(**obj.cleaned_data)
            return HttpResponse('ok')
        else:
            print('****************')
            print(obj.errors) # __str__对象
            print('****************')
            return render(request, 'login.html', {'obj':obj})

def ajax_login(request):
    import json
    ret = {'status': True, 'msg': None}
    obj = LoginFrom(request.POST)
    if obj.is_valid():
        print('****************')
        print(obj.cleaned_data)
        print('****************')
    else:
        # print('****************')
        # print(obj.errors)
        # print('****************')
        ret['status'] = False
        ret['msg'] = obj.errors
        v = json.dumps(ret)
    return HttpResponse(v)
