from django.conf.urls import url
from .views import CreatevideosView, FilesView
from rest_framework import routers
from django.urls import include,path

urlpatterns=[
    path('create/', CreatevideosView.as_view()),
    path('upload/', FilesView.as_view()),]