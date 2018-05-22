import xadmin

# Register your models here.
from xadmin import views
from . import models


class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    site_title="长风站库后台管理系统"
    site_footer="宜宾长风网络科技有限公司"
    menu_style="accordion"
xadmin.site.register(views.CommAdminView,GlobalSettings)


class WebInfoAdmin(object):
    list_display=['domain_name','title','keywords','desc']
    search_fields=['domain_name','title','keywords','desc']
    list_filter=['domain_name','title','keywords','desc']

xadmin.site.register(models.WebInfo,WebInfoAdmin)

class KeywordsAdmin(object):
    list_display=['keyword']
    search_fields=['keyword']
    list_filter=['keyword']

xadmin.site.register(models.Keywords,KeywordsAdmin)


class SearchsAdmin(object):
    list_display=['keyword']
    search_fields=['keyword']
    list_filter=['keyword']

xadmin.site.register(models.Searchs,SearchsAdmin)

