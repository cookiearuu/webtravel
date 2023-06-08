from django.shortcuts import render,redirect
import mysql.connector as sql
na=''
bi=''
em=''
add=''
phn=''
pwd1=''
pwd2=''


# Create your views here.
def signactiont(request):
    global na,bi,em,add,phn,pwd1,pwd2
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="alwaysAugustine17",database='website3')
        print(m)
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key == "name":
                na = value
            if key == "bin":
                bi = value
            if key == "email":
                em = value
            if key == "address":
                add = value
            if key == "phonenumber":
                phn = value
            if key == "password1":
                pwd1 = value
            if key =="password2":
                pwd2= value
            if "password1"=="password2":
                pwd2=value
        c = "insert into website_touragencies Values('{}','{}','{}','{}','{}','{}')".format(na,bi,em,add,phn,pwd2)
        cursor.execute(c)
        m.commit()
        print(m)

    return redirect("logint");