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
    list_display=['name','domain_name']
    search_fields=['name','domain_name']
    list_filter=['name','domain_name']

xadmin.site.register(models.WebInfo,WebInfoAdmin)