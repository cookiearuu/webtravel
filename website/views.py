import datetime
import os

from django.shortcuts import render,redirect
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import mysql.connector as sql
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator, EmptyPage
from django.core.files.storage import default_storage
from mysql.connector import cursor


import website.models
# Create your views here.
from .models import tours,touragencies,category,registeredusers,user,get_file_path,favorites,moderator,consultation

def home(request):
    return render(request,'home.html',{})

def contact(request, user_username):

    userr = user.objects.get(username=user_username)

    return render(request, 'contact.html', {'user': userr})


def mainu(request, user_username):
    userr = user.objects.get(username=user_username)
    return render(request, 'mainu.html', {'user': userr})

def consultation(request, user_username):
    # Use the user_id parameter as needed in your view logic
    # For example, retrieve the user object based on the user_id
     userr = user.objects.get(username=user_username)

     return render(request, 'consultation.html', {'user': userr})



def touragenciess(request, user_username):
    touragencies = category.objects.all()  # retrieve tour agencies or categories
    userr = user.objects.get(username=user_username)  # retrieve user object
    context = {
        'touragencies': touragencies,
        'user': userr,  # include the user object in the context
    }
    return render(request, 'touragencies.html', context)



def touragenciesview(request, category_id, user_username):
   userr = user.objects.get(username=user_username)
   if(category.objects.filter(category_id=category_id)):
       tour = tours.objects.filter(category__category_id=category_id)

       category_name=category.objects.filter(category_id=category_id).first()
       userr = user.objects.get(username=user_username)
       context = {'tours': tour,'category_id':category_id, 'category_name': category_name,'user': userr}
       return render(request,"index.html",context)
   else:
       messages.warning(request,"No such touragency found")

       return redirect('touragencies')
# def add_to_favorites(request, tour_id):
#     if request.user.is_authenticated:
#         tour = tours.objects.get(id=tour_id)
#         user_email = request.user.email
#         favorite, created = favorites.objects.get_or_create(user=user_email, tour=tour_id)
#         if created:
#             messages.success(request, "Tour added to favorites.")
#         else:
#             messages.warning(request, "Tour is already in favorites.")
#     else:
#         messages.warning(request, "Please log in to add tours to favorites.")
#     return redirect('touragencies')
def add_to_favorites(request, tour_id, user_username):
    if request.user.is_authenticated:
        tour = tours.objects.get(id=tour_id)
        user_instance = user.objects.get(username=user_username)
        user_email = user_instance.email
        favorite, created = favorites.objects.get_or_create(user_id=user_email, tour_id=tour.id)
        if created:
            messages.success(request, "Tour added to favorites.")
        else:
            messages.warning(request, "Tour is already in favorites.")
    else:
        messages.warning(request, "Please log in to add tours to favorites.")
    return redirect('touragenciess',user_username)



def tourregister(request, category_id, id, user_username):
    # Retrieve the tour object based on the id
    tour = tours.objects.get(id=id)
    userr = user.objects.get(username=user_username)
    email = userr.email  # Get the user's email

    category_name = category.objects.get(category_id=category_id)
    context = {
        'tours': tour,
        'user': userr,
        'category_id': category_id,
        'category_name': category_name,
        'user_username': user_username,
        'email': email,  # Add the user's email to the context
    }
    # Perform any necessary operations with the tour object

    # Render the tourregister.html template or perform a redirect if needed
    return render(request, 'tourregister.html', context)




@login_required
def tourss(request):
    # Get the BIN of the logged-in agency
    bin = request.session['agency'][1]

    # Filter tours by agency BIN
    tours_list = website.models.tours.objects.filter(agency__BIN=bin)

    # Create Paginator object with 5 records per page
    paginator = Paginator(tours_list, 5)

    # Get current page number from request parameters
    page_number = request.GET.get('page')

    # Get current page's tours
    page_obj = paginator.get_page(page_number)

    context = {
        'tours': page_obj,
    }

    return render(request, 'tourmain.html', context)


def  mainlogin(request):
    return render(request,'mainlogin.html',{})
def  login(request):
    return render(request,'login.html',{})
def  logint(request):
    return render(request,'logint.html',{})

def  signup(request):
    return render(request,'signup.html',{})
def  registert(request):
    return render(request,'registert.html',{})
def  register(request):
    return render(request,'register.html',{})

def  agency(request):
    return render(request,'agency.html',{})



em=''
name=''
sbjct=''
msg=''

def consulaction(request,user_username):
    global em,name,sbjct,msg
    userr = get_object_or_404(user, username=user_username)
    emailL = userr.email
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database='website3')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                name = value
            if key == "subject":
                sbjct = value
            if key == "message":
                msg = value
        c = "INSERT INTO website_consultation (email_id, name, subject, message) VALUES ('{}', '{}', '{}', '{}')".format(
            emailL, name, sbjct, msg)
        cursor.execute(c)
        m.commit()
        cursor.close()
        m.close()
        print(m)

    return redirect("consultation",user_username=user_username)


place=''
trans=''
qty=''
desc=''
img=''
price=''
agid=''



from django.core.files.storage import default_storage

def addtours(request):
    global id, place, trans, qty, desc, img, price, catid,d

    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database='website3')
        cursor = m.cursor()
        d = request.POST

        for key, value in d.items():
            if key == "id":
                id = value
            if key == "place":
                place = value
            if key == "transport":
                trans = value
            if key == "quantity":
                qty = value
            if key == "description":
                desc = value
            if key == "price":
                price = value
            if key == "categoryid":
                catid = value
            if key == "date":
                d = value

            if 'image' in request.FILES:
                image_file = request.FILES['image']
                file_path = default_storage.save(get_file_path(request, image_file.name), image_file)
                img = os.path.join('uploads/', os.path.basename(file_path))

        agency = request.session.get('agency')
        agid = agency[1]  # retrieve agency ID from session
        c = "insert into website_tours Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            id, place, trans, qty, desc, img, price, agid, catid,d)
        cursor.execute(c)
        m.commit()

    return redirect("agency_profile")



def deletetour(request, id):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database="website3")
        cursor = m.cursor()
        c = "DELETE FROM website_tours WHERE id='{}'".format(id)
        cursor.execute(c)
        m.commit()
        return redirect("agency_profile")
    else:
        return render(request, "tours")


def edittour(request, id):
    m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database="website3")
    cursor = m.cursor()

    if request.method == 'POST':
        id = request.POST['id']
        place = request.POST['place']
        transport = request.POST['transport']
        quantity = request.POST['quantity']
        description = request.POST['description']
        image = request.POST['image']
        price = request.POST['price']
        agency_id = request.POST['agency_id']
        date=request.POST['date']

        c = "UPDATE website_tours SET place=%s, transport=%s, quantity=%s, description=%s, image=%s, price=%s, agency_id=%s , date=%s WHERE id=%s"
        cursor.execute(c, (place, transport, quantity, description, image, price, agency_id, date,id))
        m.commit()

        return redirect('agency_profile')

    else:
        c = "SELECT * FROM website_tours WHERE id=%s"
        cursor.execute(c, (id,))
        result = cursor.fetchone()
        tour = {
            'id': result[0],
            'place': result[1],
            'transport': result[2],
            'quantity': result[3],
            'description': result[4],
            'image': result[5],
            'price': result[6],
            'agency_id': result[7]
        }

        return render(request, 'agency_tour', {'tour': tour})



@csrf_exempt
def load_html(request):
    if request.method == 'POST':
        filename = request.POST.get('filename')
        with open(filename, 'r') as f:
            html_content = f.read()
        return JsonResponse({'html': html_content})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def set_language(request,language_code):
    activate(language_code)
    request.session['django_language'] = language_code
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

em=''
pwd=''
def loginaction(request):
    global em,pwd
    if(request.method=="POST"):
        m=sql.connect(host="localhost",user="root",passwd="alwaysAugustine17",database="website3")
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key == "username":
                em = value
            if key == "pass":
                pwd = value
        c = "select * from website_users where username='{}' and password='{}';".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            # return render(request,'register.html')
             return redirect('register')
        else:
             return redirect('mainu')

    return redirect('mainu')

def registerbutton(request, user_username, category_id, id, registered=False):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        phone_number = request.POST.get('phonenumber')
        card_number = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        expiration_date = request.POST.get('expiration')

        userr = get_object_or_404(user, username=user_username)
        #
        #         # Get the email from the user
        emailL = userr.email


        # Get the Tour object based on the provided id
        tour = get_object_or_404(tours, id=id)

        # Create a new RegisteredUsers object
        registered_user = registeredusers(
            name=name,
            last_name=last_name,
            phone_number=phone_number,
            card_number=card_number,
            cvv=cvv,
            expiration_date=expiration_date,
            email_id=emailL,
            tour=tour
        )

        # Save the object to the database
        registered_user.save()

        # Set the 'registered' variable to True
        registered = True

        # Redirect to the desired page with the tour ID and user_username as parameters
        return redirect('touragenciesview', category_id=category_id, user_username=user_username)

    return render(request, 'index.html', {'registered': registered})


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import registeredusers



def mytours(request, user_username):
    userr = get_object_or_404(user, username=user_username)

    try:
        # Retrieve the registered tours for the user's email
        registered_tours = registeredusers.objects.filter(email=userr.email)
        registered_tourss = []


        for registered_tour in registered_tours:
            tour_info = tours.objects.get(id=registered_tour.tour_id)
            registered_tourss.append(tour_info)

    except registeredusers.DoesNotExist:
        registered_tours = []

    context = {
        'registered_tours': registered_tourss,
        'user': userr,
    }
    print(user.username)

    return render(request, 'mytours.html', context)


# def view_favorites(request, user_username):
#     user_instance = user.objects.get(username=user_username)
#     favorite_tours = favorites.objects.filter(user=user_instance)
#     context = {'favorite_tours': favorite_tours}
#     return render(request, 'favourites.html', context)
def view_favorites(request, user_username):
    user_instance = user.objects.get(username=user_username)
    favorite_tours = favorites.objects.filter(user=user_instance)
    context = {'user': user_instance, 'favorite_tours': favorite_tours}
    return render(request, 'favourites.html', context)
def user_profile(request, user_username):
    users = user.objects.get(username=user_username)
    context = {'user': users}
    return render(request, 'info.html', context)
#
# def update_user(request, user_username):
#     users = user.objects.get(username=user_username)
#
#     if request.method == 'POST':
#         new_username = request.POST.get('new_username')
#         new_email = request.POST.get('new_email')
#         new_password = request.POST.get('new_password')
#
#         if new_username:
#             users.username = new_username
#         if new_email:
#             users.email = new_email
#         if new_password:
#             users.password = new_password
#
#         users.save()
#         return redirect('user_profile', user_username=user_username)
#
#     return render(request, 'info.html', {'user': users})
from django.shortcuts import render, redirect
from .models import user

def update_user(request, user_username):
    user_instance = user.objects.get(username=user_username)

    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        new_email = request.POST.get('new_email')
        new_password = request.POST.get('new_password')

        if new_username:
            user_instance.username = new_username
        if new_email:
            user_instance.email = new_email
        if new_password:
            user_instance.password = new_password

        user_instance.save()
        return redirect('user_profile', user_username=user_instance.username)

    return render(request, 'info.html', {'user': user_instance})



def registered_users_view(request, tour_id):
    # Get the tour object based on the tour_id
    tour = get_object_or_404(tours, id=tour_id)

    # Retrieve the registered users for the tour
    registered_users = registeredusers.objects.filter(tour=tour)

    context = {
        'tour':tour,
        'registered_users': registered_users,
    }

    return render(request, 'registered_users.html', context)
def delete_favorite(request, favorite_id):
    favorite = get_object_or_404(favorites, id=favorite_id)

    if request.method == 'POST':
        favorite.delete()

    return redirect('view_favorites', user_username=favorite.user.username)

def about_tour(request, tour_id):
    tour = get_object_or_404(tours, id=tour_id)
    return render(request, 'abouttour.html', {'tour': tour})


def delete_tour(request, tour_id, user_username):
    registered_tour = get_object_or_404(registeredusers, tour_id=tour_id)

    if request.method == 'POST':
        registered_tour.delete()

    return redirect(reverse('mytours', args=[user_username]))

#
def modconsultation(request, moderator_username):

    consultations = website.models.consultation.objects.all()
    moderators = moderator.objects.get(username=moderator_username)
    context = {'consultations': consultations, 'moderator': moderators}
    return render(request,'modconsultation.html',context)

# def modconsultation(request):
#     consultations = website.models.consultation.objects.all()
#     context = {'consultations': consultations}
#     return redirect('modconsultation')

def moderator_mainu(request, moderator_username):

    tour_agencies = touragencies.objects.all()
    moderators = moderator.objects.get(username=moderator_username)
    context = {'tour_agencies': tour_agencies, 'moderator': moderators}
    return render(request, 'moderator_mainu.html', context)

# def delete_favorite(request, favorite_id):
#     favorite = get_object_or_404(favorites, id=favorite_id)
#
#     if request.method == 'POST':
#         favorite.delete()
#
#     return redirect('view_favorites', user_username=favorite.user.username)
from django.core.mail import send_mail
from django.core.mail import send_mail
#
# def moderator_response(request, moderator_username, consultation_email):
#
#     userr = get_object_or_404(user, email=consultation_email)
#     emailL = userr.email
#     print(emailL)
#     moderators = moderator.objects.get(username=moderator_username)
#
#     # Sending the email
#     subject = "Response to your consultation"
#     message = "This is the response to your consultation."
#     from_email = emailL  # Sender's email address
#     recipient_list = [consultation_email]  # Recipient's email address
#
#     send_mail(subject, message, from_email, recipient_list)
#     context = {
#         'moderator_username': moderator_username,
#         'consultation_email': consultation_email
#     }
#     return render(request, 'modresponse.html', context)


def moderator_response(request, moderator_username, consultation_email):
    users = get_object_or_404(user, email=consultation_email)
    emailL = user.email

    consultations = get_object_or_404(website.models.consultation, email=consultation_email)
    name = consultations.name
    message= consultations.message
    print(emailL)
    moderator_obj = get_object_or_404(moderator, username=moderator_username)

    if request.method == 'POST':
        response = request.POST.get('response')  # Get the response from the submitted form

        # Sending the email
        subject = f"Response to your consultation, Dear {name}"
        message = f",\n.It's answer for your this question   {message}:This is the response to your consultation: {response}"
        from_email = emailL  # Sender's email address
        recipient_list = [consultation_email]  # Recipient's email address

        send_mail(subject, message, from_email, recipient_list)

        context = {
            'moderator_username': moderator_username,
            'consultation_email': consultation_email,
            'consultations': consultations
        }
        return render(request, 'modresponse.html', context)
    #
    # context = {
    #     'moderator_username': moderator_username,
    #     'consultation_email': consultation_email
    # }
    # return render(request, 'moderator_response.html', context)



from django.shortcuts import render


def delete_tour_agency(request, id, moderator_username):
    moderators = moderator.objects.get(username=moderator_username)
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database="website3")
        cursor = m.cursor()
        c = "DELETE FROM website_touragencies WHERE BIN='{}'".format(id)
        cursor.execute(c)
        m.commit()
        return redirect("moderator_mainu",moderator_username)
    else:
        return render(request, "moderator_mainu.html")


def edit_tour_agency(request, id, moderator_username):
    m = sql.connect(host="localhost", user="root", passwd="alwaysAugustine17", database="website3")
    cursor = m.cursor()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        imagee = request.POST['imagee']

        c = "UPDATE website_touragencies SET name=%s, email=%s, address=%s, phonenumber=%s, password=%s, imagee=%s WHERE BIN=%s"
        cursor.execute(c, (name, email, address, phonenumber, password, imagee, id))
        m.commit()

        return redirect('moderator_mainu',moderator_username)

    else:
        c = "SELECT * FROM website_touragencies WHERE id=%s"
        cursor.execute(c, (id,))
        result = cursor.fetchone()
        agency = {
            'id': result[0],
            'name': result[1],
            'BIN': result[2],
            'email': result[3],
            'address': result[4],
            'phonenumber': result[5],
            'password': result[6],
            'imagee': result[7]
        }

        return render(request, 'moderator_mainu.html', {'agency': agency, 'moderator_username': moderator_username})



def moderatorresponsepage(request, moderator_username, consultation_email):

    consultations = get_object_or_404(website.models.consultation, email=consultation_email)

    userr = get_object_or_404(user, email=consultation_email)
    print("consemail: ",consultation_email)
    print("moduser: ", moderator_username)
    if request.method == 'POST':
        response = request.POST.get('response')
        # Process the response and send the email
        # Add your email sending logic here

        # Render a success or confirmation message
        context = {'success_message': 'Response sent successfully!'}
        return render(request, 'success.html', context)

    # Render the mod_response.html template for GET requests
    context = {
        'moderator_username': moderator_username,
        'consultation_email': consultation_email,
        'consultations':consultations
    }
    return render(request, 'modresponse.html', context)