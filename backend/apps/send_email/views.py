from django.shortcuts import render
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
import os
import apps.create_videos_api.vogon as vogon 
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from apps.files.models import Files
from apps.files.models import Videos
from oauth2client.tools import argparser
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files import File
from os.path import basename
from threading import Thread
from apps.create_videos_api.models import *
import apps.send_email.mailchimp_python_function as mpf
import apps.send_email.newsletter_template as newsletter_template
import pandas as pd
from mailchimp3 import MailChimp
import apps.send_email.configure as configure
from .serializers import *
# from .configure import MC_API_KEY, MC_USER_NAME
from mailchimp_marketing import Client


from threading import Thread

def send_email(pk):
    print(pk)

global preview
emails = Thread(target= send_email , args=([1]))

class SendEmail(APIView):
    def message(self, message, status, meta, data):
        res = {'message': message,
        "status": status,
        "meta": meta,
        "data":data}
        
        return res

    def get(self,reques,pk):
        global emails
        obj = self.get_obj(pk)
        if(obj is not None):
            # obj.videos.values('pk',flat=True)
            print(obj.videos.values_list('pk', flat=True))
            # print(list(obj))
            pks = obj.videos.values_list('pk', flat=True)
            videos = Videos.objects.filter(pk__in=list(pks))
            # print(videos)
            data = EmailSerializer(videos,many=True)
            data = data.data
            if (emails.is_alive()):
                print("Thread in proccess")     
                res = self.message("Tus correos estan siendo enviados",status.HTTP_202_ACCEPTED,"",data)
            else:                                                                                                                                                                                                                                                               
                print("Stat Thread")
                emails = Thread(target= self.send_email , args=([data]))
                emails.start()
                res = self.message("Tus correos seran enviados",status.HTTP_200_OK,"",data)


        return Response(res, res['status'])
        
    def get_obj(self,pk):
        try:
            obj = Campaign.objects.get(pk=pk)
            return obj
        except ObjectDoesNotExist:
            return None

    def send_email(self,data):
        audience_creation_dictionary = {
            "audience_name" : "Testing JRTEC",
            "company" : "Jrtec",
            "address1" : "Los 2 Puentes",
            "city" :  "Quito",
            "state" : "UNo",
            "zip_code" : "593",
            "country" : "EC", # FOR SRI LANKA : USE LK
            "from_name" : "Tester1",
            "from_email" : "cristhianepncobos@gmail.com",
            "language" : "es"
        }    
        
        audience_creation = mpf.audience_creation_function(audience_creation_dictionary)
        # print(audience_creation)
        if(audience_creation is not None):
            merge_creation = mpf.add_mergefield('URLVIDEO','Video usuario', 'url','',audience_creation['id'])
            # print(merge_creation)
            # data = data.data
            # print(data, type(data))
            # add_member = mpf.add_members_to_audience_function(123,data)
            print("##################### ADD MEMBER #############################")
            for member1 in data:
                add_member = mpf.add_members_to_audience_function(audience_creation['id'],member1)
                # print(add_member)

            print("##################### ADD TEMPLATE #############################")
            html_code = newsletter_template.html_code           
            template = mpf.customized_template(html_code=html_code, name="Update")
            print(template)
            print("##################### ADD CAMPAIGN #############################")

            campaign_name = 'Primera prueba de envio' #asunto
            from_name = 'Tester 1' #mensaje de nombre
            reply_to = 'cristhianepncobos@gmail.com' # test1@gmail.com  correo que envia el mensaje

            campaign = mpf.campaign_creation_function(campaign_name=campaign_name,
                                                audience_id=audience_creation['id'],
                                                from_name=from_name,
                                                reply_to=reply_to, template_id= template['id'])    
            print(campaign)
            #################### ADD MEMBER #############################
            send = mpf.send_mail(campaign['id'])    
            delete = mpf.delete_audience(audience_creation['id'])

class SendingView(APIView):

    def message(self, message, status, meta, data):
        res = {'message': message,
        "status": status,
        "meta": meta,
        "data":data}
        
        return res
    
    def get(self, request):
        global emails
        if (emails.is_alive()):
            res = self.message("Enviando videos",status.HTTP_202_ACCEPTED,"",[])
        else:
            res = self.message("Videos enviados",status.HTTP_200_OK,"",[])

        return Response(res, res['status'])