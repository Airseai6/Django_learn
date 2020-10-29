from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# mark_safe标记后Django不再对该函数的内容进行转义


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })