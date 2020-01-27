from django.forms import Form, fields
from django.shortcuts import render, HttpResponse


def test(request):
    print('test')
    return HttpResponse('execute views')


class LoginFrom(Form):
    # 正则的验证
    username = fields.CharField(max_length=18, min_length=6, required=True)
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
        if obj.is_valid():
            print(obj.cleaned_data) # 字典类型
            # .create(**obj.cleaned_data)
            return HttpResponse('ok')
        else:
            print(obj.errors) # __str__对象
            return render(request, 'login.html', {'obj':obj})

