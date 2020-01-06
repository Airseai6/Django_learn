from django.shortcuts import render, redirect, HttpResponse
from utils import sqlheper
import json


def classes(request):
    sql1 = 'select id,title from class'
    class_list = sqlheper.get_list(sql1, [])

    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html', )
    else:
        print(request.POST)
        v = request.POST.get('title')
        if len(v) > 0:
            sql1 = "insert into class(title) values(%s)"
            sqlheper.modify(sql1, [v, ])

            return redirect('/classes/')
        else:
            return render(request, 'add_class.html', {'msg': 'Your submit is None!'})


def del_class(request):
    print(request.GET)
    id = request.GET.get('nid')
    sql = "delete from class where id=%s"
    sqlheper.modify(sql, [id, ])

    return redirect('/classes/')


def edit_class(request):
    id = request.GET.get('nid')
    if request.method == 'GET':
        sql = "select id, title from class where id=%s"
        result = sqlheper.get_one(sql, [id, ])

        return render(request, 'edit_class.html', {'result': result})
    else:
        title = request.POST.get('title')
        sql2 = "update class set title=%s where id=%s"
        sqlheper.modify(sql2, [title, id, ])

        return redirect('/classes/')


def students(request):
    sql = 'select student.id,student.name, class.title from student left join class on student.class_id = class.id'
    student_list = sqlheper.get_list(sql, [])

    return render(request, 'students.html', {'student_list': student_list})


def add_student(request):
    if request.method == 'GET':
        sql = 'select id,title from class'
        class_list = sqlheper.get_list(sql, [])

        return render(request, 'add_student.html', {'class_list': class_list, })
    else:
        name = request.POST.get('name')
        if len(name) == 0:
            sql = 'select id,title from class'
            class_list = sqlheper.get_list(sql, [])
            return render(request, 'add_student.html', {'class_list': class_list, 'msg': 'Your submit is None!'})
        else:
            class_id = request.POST.get('class_id')
            sql2 = 'insert into student(name, class_id) values(%s,%s)'
            sqlheper.modify(sql2, [name, class_id, ])

        return redirect('/students/')


def edit_student(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        sql1 = 'select id, title from class'
        class_list = sqlheper.get_list(sql1, [])
        sql2 = 'select id, name, class_id from student where id=%s'
        current_student_info = sqlheper.get_one(sql2, [nid, ])
        return render(request, 'edit_student.html', {'class_list': class_list,
                                                     'current_student_info': current_student_info, })
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        print(name, class_id, nid)
        sql3 = 'update student set name=%s, class_id=%s where id=%s'
        sqlheper.modify(sql3, [name, class_id, nid, ])
        return redirect('/students/')


def del_student(request):
    id = request.GET.get('nid')
    sql = "delete from student where id=%s"
    sqlheper.modify(sql, [id, ])

    return redirect('/students/')


# ----------------------------------- Dialog Box -----------------------------------
def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sql = 'insert into class(title) values(%s)'
        sqlheper.modify(sql, [title, ])
        return HttpResponse('ok')
    else:
        return HttpResponse('ERR：内容不能为空')


def modal_edit_class(request):
    ret = {'status': True, 'message': None}
    nid = request.POST.get('nid')
    try:
        content = request.POST.get('content')
        sql = 'update class set title=%s where id=%s'
        sqlheper.modify(sql, [content, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


def modal_add_student(request):
    name = request.POST.get('name')
    title = request.POST.get('title')
    if len(title) > 0 and len(name) > 0:
        sql = 'insert into student(name, class_id) values(%s, (select class.id from class where class.title=%s));'
        sqlheper.modify(sql, [name, title, ])
        return HttpResponse('ok')
    else:
        return HttpResponse('ERR：内容不能为空')
