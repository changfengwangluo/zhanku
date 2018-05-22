import xadmin
from . import models

class CommentAdmin(object):
    list_display=['content_type','text','object_id','user']

xadmin.site.register(models.Comment,CommentAdmin)
