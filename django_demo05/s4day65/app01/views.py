from django.shortcuts import render, redirect, HttpResponse
from utils import sqlheper
from utils import sqlhelper
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
    sql = 'select student.id,student.name, student.class_id, class.title from student left join class on student.class_id = class.id'
    student_list = sqlheper.get_list(sql, [])
    sql2 = 'select id,title from class'
    class_list = sqlheper.get_list(sql2, [])

    return render(request, 'students.html', {'student_list': student_list, 'class_list': class_list, })


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
        if len(content) == 0:
            ret['status'] = False
            ret['message'] = 'ERR: 名称不能为空'
        else:
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


def modal_add_student3(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        print(name, class_id)
        if len(name) > 0:
            sql = 'insert into student(name, class_id) values(%s, %s);'
            sqlheper.modify(sql, [name, class_id, ])
        else:
            ret['status'] = False
            ret['message'] = 'ERR: name is none.'
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


def modal_edit_student(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        nid = request.POST.get('nid')
        if len(name) > 0:
            sql = 'update student set name=%s, class_id=%s where id=%s;'
            sqlheper.modify(sql, [name, class_id, nid, ])
        else:
            ret['status'] = False
            ret['message'] = 'ERR: name is none.'
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


# ----------------------------------- 多对多，以老师表展示 -----------------------------------
def teachers(request):
    # sql = 'select id, name from teacher'
    sql = """
        SELECT teacher.id as tid, teacher.name, class.title FROM teacher
            left join teacher2class on teacher.id = teacher2class.teacher_id
            left join class on class.id = teacher2class.class_id;
    """
    teacher_list = sqlheper.get_list(sql, [])
    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid] = {'tid':row['tid'], 'name':row['name'], 'titles':[row['title'],]}

    return render(request, 'teacher.html', {'teacher_list':result.values})


def add_teacher(request):
    if request.method == 'GET':
        sql = 'select id, title from class'
        class_list = sqlheper.get_list(sql, [])
        return render(request, 'add_teacher.html', {'class_list': class_list},)
    else:
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        sql2 = 'insert into teacher(name) values(%s)'
        teacher_id = sqlheper.create(sql2, [name,])
        sql3 = 'insert into teacher2class(teacher_id, class_id) values(%s, %s)'
        
        # 多次连接多次提交
        # for item in class_ids:
        #     sqlheper.modify(sql3, [teacher_id, item, ])

        # 一次连接多次提交
        # obj = sqlheper.SqlHelper()
        # for cls_id in class_ids:
        #     obj.modify(sql3, [teacher_id, cls_id, ])
        # obj.close()

        # 一次连接一次提交
        data_list = []
        for cls_id in class_ids:
            temp = (teacher_id, cls_id, )
            data_list.append(temp)

        obj = sqlhelper.SqlHelper()
        obj.multiple_modify(sql3, data_list)
        obj.close()

        return redirect('/teachers/')


def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        sql = 'select id, name from teacher where id=%s'
        obj = sqlhelper.SqlHelper()
        teacher_info = obj.get_one(sql, [nid, ])
        sql2 = 'select class_id from teacher2class where teacher_id=%s'
        class_id_list = obj.get_list(sql2, [nid, ])
        sql3 = 'select id, title from class'
        class_list = obj.get_list(sql3, [])
        obj.close()

        temp = []
        for i in class_id_list:
            temp.append(i['class_id'])

        return render(request, 'edit_teacher.html', {
            'teacher_info': teacher_info,
            'class_id_list': temp,
            'class_list': class_list,
        })
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')

        obj = sqlhelper.SqlHelper()
        # update teacher list
        sql4 = 'update teacher set name=%s where id=%s'
        obj.modify(sql4, [name, nid, ])
        # update teacher2class list, first delete after insert
        sql5 = 'delete from teacher2class where teacher_id=%s'
        obj.modify(sql5, [nid, ])

        data_list = []
        for cls_id in class_ids:
            temp = (nid, cls_id, )
            data_list.append(temp)
        # map ? lammda 
        sql6 = 'insert into teacher2class(teacher_id, class_id) values(%s, %s)'
        obj = sqlhelper.SqlHelper()
        obj.multiple_modify(sql6, data_list)
        obj.close()

        return redirect('/teachers/')


def get_all_class(request):
    # 以后的操作可能会费时间，现在假设费时间，增加loading界面
    import time
    time.sleep(0.4)
    obj = sqlhelper.SqlHelper()
    sql = 'select id, title from class'
    class_list = obj.get_list(sql, [])
    obj.close()
    return HttpResponse(json.dumps(class_list))


def modal_edit_teacher(request):
    ret = {'status':True, 'message':None,}
    try:
        name = request.POST.get('name')
        class_id_list = request.POST.getlist('class_id_list')

        cur = sqlhelper.SqlHelper()
        sql = 'insert into teacher(name) values(%s)'
        teacher_id = cur.create(sql, [name, ])

        data_list = []
        for cls_id in class_id_list:
            temp = (teacher_id, cls_id, )
            data_list.append(temp)
        
        sql2 = 'insert into teacher2class(teacher_id, class_id) values(%s, %s)'
        cur.multiple_modify(sql2, data_list,)
        cur.close()

    except Exception as e:
        ret['status'] = False
        ret['message'] = 'ERR: ' + str(e)
    
    return HttpResponse(json.dumps(ret))
