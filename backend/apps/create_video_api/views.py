from django.shortcuts import render
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

class CreatevideosView(APIView):

    def message(self, message, status, meta, data):
        res = {'message': message
        "status": status,
        "meta": meta,
        "data":data}
        
    # Create your views here.
    # context = {'video': video, 'load': load }
    # template_name = 'index.html'
    # video_path = "Project/assets/base_video.mp4"

    def get(self):
            path_dir= os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project") 
            config_file= os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project/config.json")
            print(path_dir)
            print(config_file)
            vogon.generate_preview(self.config_file,1,self.path_dir)
            print(self.context)
            # preview = Thread(target= self.generate_preview , args=(request,self.config_file,1,self.path_dir))
            preview.start()
            # self.context['video']=100
        return render(request, self.template_name,self.context,)

    def generate_preview(self,request,config_file, number,path_dir):
        vogon.generate_preview(config_file,number, path_dir)    
        self.context['load'] = 0
        self.context['video']=100
        print(self.context)
        self.get(request)
        # return render_to_response(self.template_name,context=self.context)
        # return redirect(to='/')
        # return redirect('')
