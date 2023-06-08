from django.shortcuts import render,redirect
import mysql.connector as sql
from website.views import register
em=''
un=''
pwd=''
def signaction(request):
    global em,un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="alwaysAugustine17",database='website3')
        print(m)
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "username":
                un = value
            if key == "password1":
                pwd = value
        c = "insert into website_user Values('{}','{}','{}')".format(em,un,pwd)
        cursor.execute(c)
        m.commit()
        print(m)

    return redirect("login")



