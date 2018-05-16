from django.shortcuts import render,get_object_or_404,render_to_response,get_list_or_404
from .models import WebInfo

# Create your views here.

def index(request):

    return render(request,'index.html')

def list(request):
    webs=get_list_or_404(WebInfo,)
    return render(request, 'list.html')

def info(request,web_id):
    web=get_object_or_404(WebInfo,pk=web_id)

    return render_to_response('info.html',{'web':web})

def search(request,keywords):

    webs = get_list_or_404(WebInfo, )
    return render(request, 'list.html')





