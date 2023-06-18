import logging
from .models import *
from coolsite import settings
from django.core.cache import cache
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import HttpResponse

error_logger=logging.getLogger('error_logger')

def cache_handler(context,dict,options={'is_top_services':False}):
    for i in dict.keys():
            if(not options['is_top_services'] and i=='services_top'):
                continue
            elif(options['is_top_services'] and i=='services'):
                continue

            cache_data=cache.get(i)
            try:
                if not cache_data:
                    data=dict[i]()

                    if(i=='cats'):
                        for cat in data:
                            cat.posts_count=cat.post_set.count()

                    cache.set(i,data,600)

            except Exception as exc:
                error_logger.error("STATUS - 500, {0}".format(exc))
                return HttpResponse(status=500)

            if(i=='services_top' or i=='services'):
                context['services']=cache_data or data
            else:   
                context[i]=cache_data or data
            
                
class DataMixin:
    def get_user_context(self,request,is_top_services=True,**kwargs):
        context=kwargs

        context['media_url']=settings.MEDIA_URL
        context['add_message_form']=AddMessage()
        context['user_id']=request.session.get('user_id','None')

        fields_dict={
            'clients':lambda :User.objects.filter(is_client=True),
            'responses': lambda :Response.objects.all().order_by('-time_create').select_related('user'),
            'services_top':lambda :Service.objects.filter(is_top=True)[:3],
            'services':lambda: Service.objects.all(),
        }

        cache_handler(context,fields_dict,{'is_top_services':is_top_services})

        paginator=Paginator(context['responses'],2)
        if request.GET.get('c_page'):
            page=paginator.get_page(int(request.GET.get('c_page')))
        else:
            page=paginator.get_page(1)
        
        context['c_page_obj']=page

        return context

def edit_data(obj,is_expanded=False):
    obj.day=obj.time_create.strftime("%d")
    if(is_expanded):
        obj.mounth=obj.time_create.strftime("%B")
        obj.year=obj.time_create.strftime("%Y")
    else:
        obj.mounth=obj.time_create.strftime("%b")

    del obj.time_create

def is_auth_handler(request,redirect_to='login'):
    if request.GET.get('user_id')=='None':
        return redirect(redirect_to)
    else:
        return True