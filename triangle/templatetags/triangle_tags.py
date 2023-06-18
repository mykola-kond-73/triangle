from django import template
from triangle.models import *

register=template.Library()

@register.inclusion_tag('triangle/paginator.html')
def paginator(page_obj,attr_name='page',anchor=None):
    return {"page_obj":page_obj,'anchor':anchor,'attr_name':attr_name}  

@register.inclusion_tag('triangle/comments.html')
def comments(comments,media_url,post,user_id):
    return {'comments':comments,'media_url':media_url,'post':post,'user_id':user_id}