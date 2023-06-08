
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from login.views import loginaction
from website import views
urlpatterns = [
    path('login/',loginaction),
    # path('registert/',signaction),
    # path('logint/',loginaction),
]