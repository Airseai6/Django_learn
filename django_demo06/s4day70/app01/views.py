from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse


def index(request):
    user_list = [
        'alex', 'eric', 'tony',
    ]
    v = reverse('n1')
    print(v)
    return render(request, 'index.html', {'user_list':user_list})


def edit(request, a1):
    print(a1)
    return HttpResponse('...')
