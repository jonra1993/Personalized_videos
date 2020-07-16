from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.template import Template,Context, loader
from django.views import View 
import django.forms
import vogon

def index (request):
    if(request.GET.get('Generar')):
        print("holiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

    return render(request,'index.html')

    # return render_to_response('index.html')

# class Index(View)
class Index(View):
    template_name = 'index.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self, request):
        if request.method == 'POST' and 'generar' in request.POST:
            print("Holiiiiiiiiiiiiiiii")
        return render(request, self.template_name,)




def about_us(request):

    # render('aboutUs.html')
    return render_to_response('aboutUs.html' )




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