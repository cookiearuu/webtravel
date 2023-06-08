
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from login.views import loginaction
from registert.views import signactiont
urlpatterns = [
    path('registert/',signactiont),

]