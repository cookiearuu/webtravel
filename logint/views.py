from django.shortcuts import render
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
biin=''
pwd=''
# def loginactiont(request):
#     global biin,pwd
#     if(request.method=="POST"):
#         m=sql.connect(host="localhost",user="root",passwd="alwaysAugustine17",database="website3")
#         cursor=m.cursor()
#         d=request.POST
#         for key, value in d.items():
#             if key == "biin":
#                 biin = value
#             if key == "pass":
#                 pwd = value
#         c = "select * from website_touragencies where BIN='{}' and password='{}';".format(biin, pwd)
#         cursor.execute(c)
#         t = tuple(cursor.fetchall())
#         if t == ():
#             # return render(request,'home.html')
#             return redirect('registert')
#
#         else:
#             return redirect('tourss')
#
#     return render(request, 'home.html')



#
# def agency_profile(request):
#     agency = request.session.get('agency')
#     if not agency:
#         return redirect('login')  # если агентство не зарегистрировано, перенаправляем на страницу логина
#     return render(request, 'agency.html', {'agency': agency})


def agency_profile(request):
    agency = request.session.get('agency')
    if not agency:
        return redirect('login')

    # Extract necessary fields from agency tuple
    name, BIN, email, address, phonenumber, imagee = agency

    context = {
        'agency': {
            'name': name,
            'BIN': BIN,
            'email': email,
            'address': address,
            'phonenumber': phonenumber,
            'imagee': imagee
        }
    }

    return render(request, 'agency.html', context)


def loginactiont(request):
    if(request.method=="POST"):
        m=sql.connect(host="localhost",user="root",passwd="alwaysAugustine17",database="website3")
        cursor=m.cursor()
        d=request.POST
        biin = d.get("biin")
        pwd = d.get("pass")
        c = "select * from website_touragencies where BIN='{}' and password='{}';".format(biin, pwd)
        cursor.execute(c)
        t = cursor.fetchone() # Use fetchone() instead of fetchall()
        if t is None:
            return redirect('registert')
        else:
            # Unpack the single tuple item into separate variables
            name, BIN, email, address, phonenumber, image, *extra_cols = t
            request.session['agency'] = name, BIN, email, address, phonenumber, image

            return redirect('agency_profile')
    return render(request, 'home.html')