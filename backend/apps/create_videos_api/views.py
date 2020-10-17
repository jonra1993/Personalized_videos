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


class CreatevideosView(APIView):

    def message(self, message, status, meta, data):
        res = {'message': message,
        "status": status,
        "meta": meta,
        "data":data}
        
        return res
        

    def post(self, request):
        data = request.data
        serializer = CreateSerializer(data = data)
        if(serializer.is_valid()):
            obj = self.get_obj(data['pk'])
            if(obj is not None):
                project_dir = os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project") 
                config_file = os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project/config.json")
                print(project_dir)
                print(config_file)
                # vogon.generate_videos_final(config_file, Non,path_dir)
                # vogon.generate_videos_final(config_file, None,path_dir)
                # vogon.generate_preview(config_file,1,path_dir)
                config = vogon.load_config(config_file)
                data = vogon.read_csv_file_database(obj.csv_file.pk,',')
                lines = enumerate(data)
                for i, row in lines:
                    video = vogon.generate_video(config, row, (i + 1), project_dir)
                    print("VIDEO PATH", video)
                    print("VIDEO TYPE", type(video))
                    local_file = open(video, 'rb')   
                    print("VIDEO TYPE", type(local_file))
                    djangofile = File(local_file, name=video)
                    video_obj = Videos.objects.create(video= djangofile, first_name =row['Nombre'], last_name=row['Apellido'])
                    obj.videos.add(video_obj)
                    os.remove(video)
                ser = CreateGetSerializer(obj)

                res = self.message("Videos creados",status.HTTP_200_OK,"",ser.data)
            else:
                res = self.message("Campana no creada",status.HTTP_200_OK,"",[])
        else:
            res = self.message("Error",status.HTTP_200_OK,"",[])

        return Response(res, res['status'])
        # return Response("holi")

    def get_obj(self,pk):
        try:
            obj = Campaign.objects.get(pk=pk)
            return obj
        except ObjectDoesNotExist:
            return None

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
            res = self.message("Camapana creada exitosamente",status.HTTP_201_CREATED,"",serializer.data )      

        else:
            res = self.message("Datos erroneos", status.HTTP_400_BAD_REQUEST,"",[])
        return Response(res, res['status'])


    def get(self, request):
        res = self.message("OK funciona mucho", status.HTTP_200_OK,"",[])
        return Response(res, res['status'])



