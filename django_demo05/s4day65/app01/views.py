from django.shortcuts import render, redirect
import pymysql
from utils import sqlheper

def classes(request):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='s4db65',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id,title from class')
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html', )
    else:
        print(request.POST)
        v = request.POST.get('title')
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='s4db65',
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(title) values(%s)", v)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/classes/')


def del_class(request):
    print(request.GET)
    id = request.GET.get('nid')
    print(id)
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='s4db65',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s", id)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/classes/')


def edit_class(request):
    id = request.GET.get('nid')
    if request.method == 'GET':
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='s4db65',
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id, title from class where id=%s", id)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, 'edit_class.html', { 'result': result})
    else:
        title = request.POST.get('title')
        print(title)
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='s4db65',
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id=%s", [title, id,])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/classes/')


def students(request):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='s4db65',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select student.id,student.name, class.title from student left join class on student.class_id = class.id')
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'students.html', {'student_list': student_list})


def add_student(request):
    if request.method == 'GET':
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='s4db65',
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select id,title from class')
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()

        return render(request, 'add_student.html', {'class_list':class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='s4db65',
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('insert into student(name, class_id) values(%s,%s)',[name, class_id,])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/students/')


def edit_student(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        sql1 = 'select id, title from class'
        class_list = sqlheper.get_list(sql1, [])
        sql2 = 'select id, name, class_id from student where id=%s'
        current_student_info = sqlheper.get_one(sql2, [nid,])
        return render(request, 'edit_student.html', {'class_list':class_list,
                                                     'current_student_info': current_student_info,})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        print(name, class_id, nid)
        sql3 = 'update student set name=%s, class_id=%s where id=%s'
        sqlheper.modify(sql3, [name, class_id, nid,])
        return redirect('/students/')
