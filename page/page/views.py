from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response 
from django.template import Template,Context, loader
from django import forms
from django.views import View 
import page.vogon as vogon
import os 
from threading import Thread

class Index(View):
    video = 10
    load = 0
    context = {'video': video, 'load': load }
    template_name = 'index.html'
    path_dir= os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project") 
    config_file= os.path.join (os.path.dirname(os.path.abspath(__file__)) ,"Project/config.json")
    video_path = "Project/assets/base_video.mp4"
    print(type(config_file))


    def get(self,request):
        return render(request,self.template_name,self.context)

    def post(self, request):
        if request.method == 'POST' and 'generar' in request.POST:
            print("Holiiiiiiiiiiiiiiii")
            # print(os.path.dirname(os.path.abspath(__file__)) )
            print(self.path_dir)
            print(self.config_file)
            self.context['load']=1
            # vogon.generate_preview(self.config_file,1,self.path_dir)
            print(self.context)
            preview = Thread(target= self.generate_preview , args=(request,self.config_file,1,self.path_dir))
            preview.start()
            # self.context['video']=100
        return render(request, self.template_name,self.context,)

    def generate_preview(self,request,config_file, number,path_dir):
        # vogon.generate_preview(config_file,number, path_dir)    
        self.context['load'] = 0
        self.context['video']=100
        print(self.context)
        self.get(request)
        # return render_to_response(self.template_name,context=self.context)
        # return redirect(to='/')
        # return redirect('')


def about_us(request):

    # render('aboutUs.html')
    return render_to_response('aboutUs.html' )


def preview(request):
    aux = 0
    context= {'aux': aux}
    return render(request,'preview.html',context)

    # return render_to_response('preview.html' )



# def index (request):
#     # Template()
#     # plt = loader.get_template('index.html')
#     plt = Template(loader.get_template('index.html'))
#     # plt = Template('index.html')
#     ctx= Context()
#     document = plt.render(ctx)
#     return HttpResponse(document)

# def about_us (request):

#     plt = open)

#     documento = rend
#     return