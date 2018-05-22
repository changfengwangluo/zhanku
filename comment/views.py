from django.shortcuts import render,redirect
from .models import Comment
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def comment(request):
    user=request.user
    text=request.POST.get('text','')
    content_type=request.POST.get('content_type','')
    object_id=int( request.POST.get('object_id',''))
    #通过contenttypes得到所关联的对象
    model_class=ContentType.objects.get(model=content_type).model_class()
    model_obj=model_class.objects.get(pk=object_id)

    cmt=Comment()
    cmt.user=user
    cmt.text=text
    cmt.content_type=content_type
    cmt.object_id=object_id
    cmt.content_object=model_obj
    cmt.save()

    return redirect(request.META.get('HTTP_REFERER'))