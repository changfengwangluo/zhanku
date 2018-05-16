
from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list),#列表页
    path('info/<int:web_id>', views.info),#详情页
]