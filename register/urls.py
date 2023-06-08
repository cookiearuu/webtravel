
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from login.views import loginaction
from register.views import signaction
from website import views
urlpatterns = [
    path('register/',signaction),
    path('login/',loginaction),
]