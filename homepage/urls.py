from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'homepage'

urlpatterns = [
    path('', views.login_view, name="login"),
    path('compose/', views.compose_view, name="compose"),
    path('inbox/', views.inbox_view, name="inbox"),
    path('sent/', views.sent_view, name="sent"),
    path('trash/', views.trash_view, name="trash"),
    path('options/', views.options_view, name="options")
]
