from django.shortcuts import render


def classes(request):
    import pymysql
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
