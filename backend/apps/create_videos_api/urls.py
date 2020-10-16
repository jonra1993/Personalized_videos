from django.conf.urls import url
from .views import CreatevideosView
from rest_framework import routers
from django.urls import include,path

urlpatterns=[
    path('create/', CreatevideosView.as_view()),
]