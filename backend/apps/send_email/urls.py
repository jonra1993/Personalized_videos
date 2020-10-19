from django.conf.urls import url
from .views import CreatevideosView, FilesView
from rest_framework import routers
from django.urls import include,path

urlpatterns=[
    path('send/', FilesView.as_view()),]