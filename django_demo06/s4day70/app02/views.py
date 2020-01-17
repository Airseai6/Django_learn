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
