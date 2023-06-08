from django.shortcuts import render
from django.shortcuts import render, redirect
import mysql.connector as sql

from website.models import user,moderator
from website.views import login
from website import views
# Create your views here.
# em=''
# pwd=''
# def loginaction(request):
#     global em,pwd
#     if(request.method=="POST"):
#         m=sql.connect(host="localhost",user="root",passwd="alwaysAugustine17",database="website3")
#         cursor=m.cursor()
#         d=request.POST
#         for key, value in d.items():
#             if key == "username":
#                 em = value
#             if key == "pass":
#                 pwd = value
#         c = "select * from website_user where username='{}' and password='{}';".format(em, pwd)
#         cursor.execute(c)
#         t = tuple(cursor.fetchall())
#         if t == ():
#             # return render(request,'register.html')
#              return redirect('register')
#         else:
#              return redirect('mainu', user_username=em)
#
#
#     return redirect('mainu')


em = ''
pwd = ''
#
# def loginaction(request):
#     global em, pwd
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database="website3")
#         cursor = m.cursor()
#         d = request.POST
#         for key, value in d.items():
#             if key == "username":
#                 em = value
#             if key == "pass":
#                 pwd = value
#         c = "SELECT * FROM website_user WHERE username='{}' AND password='{}';".format(em, pwd)
#         cursor.execute(c)
#         t = tuple(cursor.fetchall())
#         if t == ():
#             # return render(request,'register.html')
#             return redirect('register')
#         else:
#             return redirect('mainu', user_username=em)
#
#     return redirect('mainu', user_username=em)
#
# def loginaction(request):
#     if request.method == "POST":
#         em = request.POST.get("username")
#         pwd = request.POST.get("pass")
#
#         # Check if the username and password exist in the user table
#         users = user.objects.filter(username=em, password=pwd).first()
#
#         if not users:
#             # Check if the username and password exist in the moderators table
#             moderators = moderator.objects.filter(username=em, password=pwd).first()
#             if moderators:
#                 # Redirect to the moderator page
#                 return redirect('moderator_mainu',user_username=em)
#
#             # Username and password not found in both user and moderator tables
#             return redirect('register')
#
#         # Redirect to the main user page
#         return redirect('mainu', user_username=em)
#
#     return redirect('mainu')


def loginaction(request):
    if request.method == "POST":
        em = request.POST.get("username")
        pwd = request.POST.get("pass")

        # Check if the username and password exist in the user table
        users = user.objects.filter(username=em, password=pwd).first()

        if not users:
            # Check if the username and password exist in the moderators table
            moderators = moderator.objects.filter(username=em, password=pwd).first()
            if moderators:
                # Redirect to the moderator page
                return redirect('moderator_mainu', moderator_username=em)

            # Username and password not found in both user and moderator tables
            return redirect('register')

        # Redirect to the main user page
        return redirect('mainu', user_username=em)

    return redirect('mainu')



























