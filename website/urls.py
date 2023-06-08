
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.urls import include

import logint.views
from login.views import loginaction
from logint.views import *
from register.views import signaction
from registert.views import signactiont
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import consulaction, addtours, deletetour, edittour, add_to_favorites, moderator_response, \
    moderatorresponsepage

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

#without logging in FOR TOURS AND FOR USERS
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('mainu/<str:user_username>/consultation/',views.consultation,name="consultation"),
    path('mainu/<str:user_username>/contact/', views.contact, name='contact'),
    path('mainu/<str:user_username>/mytours/', views.mytours, name='mytours'),

                  #LOGIN PAGE
    path('mainlogin/', views.mainlogin, name="mainlogin"),
    path('login', views.login, name="login"),
    path('logint', views.logint, name="logint"),
    path('agency/profile/',logint.views.agency_profile,name='agency_profile'),
#SIGN UP PAGE
    path('signup', views.signup, name="signup"),
    path('register', views.register, name="register"),
    path('registert', views.registert, name="registert"),

#LOG IN AND REGISTER BUTTONS
    path('register/',signaction),
    path('login/',loginaction),
    path('registert/',signactiont),
    path('logint/',loginactiont),
    path('mainu/<str:user_username>/consultation/consulaction/',consulaction,name='consulaction'),

#USERS AFTER LOGGIN ING
    path('mainu/<str:user_username>/', views.mainu, name='mainu'),



#TOURS AFTER LOGGIN IN
    path('mainlogin', views.mainlogin, name="mainlogin"),
    path('mainu/<str:user_username>/touragenciess/', views.touragenciess, name="touragenciess"),
    path('mainu/<str:user_username>/touragencies/<int:category_id>/', views.touragenciesview, name="touragenciesview"),
    #
    # path('touragenciess/<int:category_id>/', views.touragenciesview, name="touragenciesview"),
    path('tourss/', views.tourss, name="tourss"),

#TOURACTIONS  NOT TOUR AGENCY

    path('agency/profile/addtours/',addtours),
    path('deletetour/<int:id>/', deletetour, name='deletetour'),
    path('edittour/<int:id>/', edittour, name='edittour'),



#REGISTER
    path('mainu/<str:user_username>/touragencies/<int:category_id>/tourregister/<int:id>/', views.tourregister, name='tourregister'),

    path('set-language/<str:language_code>/', views.set_language, name='set_language'),

    path('mainu/<str:user_username>/touragencies/<int:category_id>/tourregister/<int:id>/registerbutton/', views.registerbutton, name='registerbutton'),

    path('add_to_favorites/<int:tour_id>/<str:user_username>/', views.add_to_favorites, name='add_to_favorites'),
    path('mainu/<str:user_username>/favorites/', views.view_favorites, name='view_favorites'),
    path('profile/<str:user_username>/', views.user_profile, name='user_profile'),
    path('update/<str:user_username>/', views.update_user, name='update_user'),
    path('registered_users/<int:tour_id>/', views.registered_users_view, name='registered_users'),
    path('abouttour/<int:tour_id>/', views.about_tour, name='about_tour'),
    path('favorites/delete/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),
    path('mytours/delete/<int:tour_id>/<str:user_username>/', views.delete_tour, name='delete_tour'),
    path('moderatormainu/<str:moderator_username>/', views.moderator_mainu, name='moderator_mainu'),

    path('moderatormainu/<str:moderator_username>/modconsultation/', views.modconsultation, name='modconsultation'),
    path('moderatorresponsepage/<str:moderator_username>/<str:consultation_email>/',moderatorresponsepage, name='moderatorresponsepage'),
    path('moderatorresponse/<str:moderator_username>/<str:consultation_email>/', moderator_response, name='moderator_response'),

    path('delete_agency/<int:id>/<str:moderator_username>/', views.delete_tour_agency, name='delete_agency'),
    path('edit_agency/<str:id>/<str:moderator_username>/', views.edit_tour_agency, name='edit_agency'),


                  # path('manage_tour_agencies/', views.manage_tour_agencies, name='manage_tour_agencies'),


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
    path('mainu', views.mainu, name="mainu"),
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
]


