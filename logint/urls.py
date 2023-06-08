
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from logint.views import loginactiont, agency_profile
from registert.views import signactiont
urlpatterns = [
    path('logint/',loginactiont),
    path('agency/profile/',agency_profile),
   path('agency/profile/tourss',agency_profile),
]