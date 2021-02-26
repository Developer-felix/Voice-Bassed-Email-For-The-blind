from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
admin.site.site_header="Voice bassed Email"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
]
