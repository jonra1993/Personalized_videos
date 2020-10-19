from django.conf.urls import url
from .views import SendEmail, SendingView
from rest_framework import routers
from django.urls import include,path

urlpatterns=[
    path('send/<int:pk>', SendEmail.as_view()),
    path('send/', SendingView.as_view()),
    ]