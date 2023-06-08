
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from website import views
from register.views import signaction
from login.views import loginaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
