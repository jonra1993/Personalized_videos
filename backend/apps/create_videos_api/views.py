from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
import os
import apps.create_videos_api.vogon as vogon 
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from .serializers import *
from .models import *

class CreatevideosView(APIView):

    def message(self, message, status, meta, data):
        res = {'message': message,
        "status": status,
        "meta": meta,
        "data":data}
        
        return res
        
    # Create your views here.
    # context = {'video': video, 'load': load }
    # template_name = 'index.html'
    # video_path = "Project/assets/base_video.mp4"

    def post(self, request):
            path_dir= os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project") 
            config_file= os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project/config.json")
            print(path_dir)
            print(config_file)
            vogon.generate_videos_final(config_file, 2,path_dir)
            # vogon.generate_videos_final(config_file, None,path_dir)
            # vogon.generate_preview(config_file,1,path_dir)
            res = self.message("Videos creados",status.HTTP_200_OK,"",[])
            return Response(res, res['status'])
            # return Response("holi")

    
    # def generate_preview(self,request,config_file, number,path_dir):
    #     vogon.generate_preview(config_file,number, path_dir)    
    #     self.context['load'] = 0
    #     self.context['video']=100
    #     print(self.context)
    #     self.get(request)
    #     # return render_to_response(self.template_name,context=self.context)
    #     # return redirect(to='/')
    #     # return redirect('')

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
        if( serializers.is_valid() ):
            obj = Campaign.objects.create(**data)
            serializer = FileGetSerializer(obj)
            res = self.message("Camapana creada exitosamente",status.HTTP_201_CREATED,"",serializer.data )      

        else:
            res = self.message("Datos erroneos", status.HTTP_400_BAD_REQUEST,"",[])
        