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

def marketing_video(pk):
    print(pk)

global preview
preview = Thread(target= marketing_video , args=([1]))

class CreatevideosView(APIView):

    def message(self, message, status, meta, data):
        res = {'message': message,
        "status": status,
        "meta": meta,
        "data":data}
        
        return res
    
    def get(self, request):
        global preview
        if (preview.is_alive()):
            res = self.message("Creando videos",status.HTTP_400_BAD_REQUEST,"",[])
        else:
            res = self.message("Videos creados",status.HTTP_200_OK,"",[])

        return Response(res, res['status'])
        

    def post(self, request):
        global preview
        data = request.data
        serializer = CreateSerializer(data = data)
        if(serializer.is_valid()):
            obj = self.get_obj(data['pk'])
            if(obj is not None):
                print(preview.is_alive())
                if (preview.is_alive()):
                    print("Thread in proccess")                                                                                                                                                                                                                                                             
                    ser = CreateGetSerializer(obj)
                    res = self.message("Creando videos",status.HTTP_400_BAD_REQUEST,"",ser.data)
                else:                                                                                                                                                                                                                                                               
                    print("Stat Thread")
                    preview = Thread(target= self.marketing_video , args=([data['pk']]))
                    preview.start()
                    ser = CreateGetSerializer(obj)
                    res = self.message("Inicio de la creacion de videos",status.HTTP_200_OK,"",ser.data)
                #     res = self.message("Creando videos",status.HTTP_403_FORBIDDEN,"",[])
                # else:

                # project_dir = os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project") 
                # config_file = os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project/config.json")
                # print(project_dir)
                # print(config_file)
                # config = vogon.load_config(config_file)
                # data = vogon.read_csv_file_database(obj.csv_file.pk,',')
                # lines = enumerate(data)
                # for i, row in lines:
                #     video = vogon.generate_video(config, row, (i + 1), project_dir)
                #     print("VIDEO PATH", video)
                #     print("VIDEO TYPE", type(video))
                #     local_file = open(video, 'rb')   
                #     print("VIDEO TYPE", type(local_file))
                #     djangofile = File(local_file, name=video)
                #     # djangofile = File(local_file, name=row['Nombre']+"_"+row['Apellido']+".mp4")
                #     video_obj = Videos.objects.create(video= djangofile, first_name =row['Nombre'], last_name=row['Apellido'])
                #     obj.videos.add(video_obj)
                #     os.remove(video)
            else:
                res = self.message("Campana no creada",status.HTTP_200_OK,"",[])
        else:
            res = self.message("Error",status.HTTP_200_OK,"",serializer.errors)

        return Response(res, res['status'])
        # return Response("holi")

    def get_obj(self,pk):
        try:
            obj = Campaign.objects.get(pk=pk)
            return obj
        except ObjectDoesNotExist:
            return None

    def marketing_video(self, pk):
        print(pk)
        obj = self.get_obj(pk)
        project_dir = os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project") 
        config_file = os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project/config_1.json")
        print(project_dir)
        print(config_file)
        config = vogon.load_config(config_file)
        data = vogon.read_csv_file_database(obj.csv_file.pk,',')
        print(data)
        lines = enumerate(data)
        for i, row in lines:
            video = vogon.generate_video(config, row, (i + 1), project_dir)
            # video = vogon.generate_video(config, data[1],2, project_dir)
            print("VIDEO PATH", video)
            print("VIDEO TYPE", type(video))
            local_file = open(video, 'rb')   
            print("VIDEO TYPE", type(local_file))
            djangofile = File(local_file, name=row['Nombre']+video)
            # djangofile = File(local_file, name=row['Nombre']+"_"+row['Apellido']+".mp4")
            video_obj = Videos.objects.create(video= djangofile, first_name =row['Nombre'], last_name=row['Apellido'])
            obj.videos.add(video_obj)
            os.remove(video)

class FilesView(APIView):
    parser_classes =[JSONParser, MultiPartParser,FormParser]
        
    def message(self, message, status, meta, data):
        res = {'message': message,
        "status": status,
        "meta": meta,
        "data":data}
        
        return res

    def post(self, request):
        data = request.data
        serializer = FilePostSerializer(data=data)
        if( serializer.is_valid() ):
            file = Files.objects.create(file = data['csv_file'])
            obj = Campaign.objects.create(campaign= data['campaign'], csv_file = file)
            serializer = FileGetSerializer(obj)
            res = self.message("CSV cargado  exitosamente",status.HTTP_200_OK,"",serializer.data )      

        else:
            res = self.message("Datos erroneos", status.HTTP_400_BAD_REQUEST,"",serializer.errors)
        return Response(res, res['status'])


    def get(self, request):
        res = self.message("OK funciona mucho", status.HTTP_200_OK,"",[])
        return Response(res, res['status'])



class HealthyView(APIView):
    def get(self,request):
        return Response("OK", status.HTTP_200_OK)

