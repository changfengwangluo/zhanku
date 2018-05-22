from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import WebInfo


# Create your views here.

def index(request):
    return render(request, 'index.html')


def list(request):
    return render(request, 'web/list.html')


def info(request, web_id):
    web = get_object_or_404(WebInfo, pk=web_id)

    if not request.COOKIES.get('web_%s_readed' % web_id):  # cookie控制阅读数
        pass

    context = {}
    context['web'] = web

    response = render(request, 'web/info.html', context)  # 通过cookie控制阅读数
    response.set_cookie('web_%s_readed' % web_id, 'true', max_age=60)  # 有效时间60秒

    return response
