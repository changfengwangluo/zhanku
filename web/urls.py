from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list,name='list'),#列表页
    path('info/<str:web_id>', views.info,name='info'),#详情页
]