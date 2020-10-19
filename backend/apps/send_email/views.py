from django.shortcuts import render
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
import os
import apps.create_videos_api.vogon as vogon 
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from .serializers import *
from .models import *
from apps.files.models import Files
from apps.files.models import Videos
from oauth2client.tools import argparser
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files import File
from os.path import basename
from threading import Thread


class SendEmail(APIView):
    def get(self,reques,pk):
        