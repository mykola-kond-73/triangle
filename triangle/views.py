from ast import Return
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView,DetailView,CreateView
from django.shortcuts import get_object_or_404, render,redirect
from django.views.decorators.csrf import csrf_exempt
import math
import logging
from .utils import *
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

info_logger=logging.getLogger('info_logger')
error_logger=logging.getLogger('error_logger')

class Index(DataMixin,TemplateView):
    def get(self,request):
        ctx={}
        
        c_def=self.get_user_context(request,title='Triangle')
        context=dict(list(ctx.items())+list(c_def.items()))

        return render(request,'triangle/index.html',context=context)

class Aboutus(DataMixin,TemplateView):
    template_name='triangle/aboutus.html'
    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        field_dict={
            'employees':lambda :Employee.objects.all(),
            'employees_item_count':lambda :range(math.ceil((Employee.objects.all().count())/4))
        }
        cache_handler(context,field_dict)
        

        c_def=self.get_user_context(self.request,title='About Us')
        context=dict(list(context.items())+list(c_def.items()))

        employees_two_dimensional=[]
        for i in context['employees_item_count']:
            employees_length=len(context['employees'])-i*4
            if employees_length >= 4:
                employees_two_dimensional.append(context['employees'][i*4:4])
            else:
                employees_two_dimensional.append(context['employees'][i*4:])

        context['employees']=employees_two_dimensional
        return context

class Sercices(DataMixin,TemplateView):
    template_name='triangle/service.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        
        field_dict={
            'projects': lambda :Project.objects.all().values('photo_small','name')[:8]
        }
        cache_handler(context,field_dict)

        c_def=self.get_user_context(self.request,is_top_services=False,title='Services')
        context=dict(list(context.items())+list(c_def.items()))

        return context

class Pricings(DataMixin,TemplateView):
    template_name='triangle/pricing.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        field_dict={
            'pricings':lambda :Pricing.objects.all()
        }
        cache_handler(context,field_dict)

        c_def=self.get_user_context(self.request,title='Pricing')
        context=dict(list(context.items())+list(c_def.items()))

        return context

class Contacts(DataMixin,TemplateView):
    template_name='triangle/contact.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        c_def=self.get_user_context(self.request,title='Contact Us')
        context=dict(list(context.items())+list(c_def.items()))

        return context

class Blog(DataMixin,ListView):
    model=Post
    template_name='triangle/blog.html'
    context_object_name='posts'
    extra_context={'title':'Blog'}
    allow_empty: False

    paginate_by= 3

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        field_dict={
            'tags':lambda :Tag.objects.all(),
            'posts_count':lambda :Post.objects.count(),
            'cats':lambda :list(Category.objects.all().prefetch_related('post_set')),

        }
        cache_handler(context,field_dict)

        c_def=self.get_user_context(self.request,cat_slug=self.request.GET.get('cat',''))
        context=dict(list(context.items())+list(c_def.items()))

        return context
    
    def get_queryset(self):
        try:
            cat=self.request.GET.get('cat')
            tag=self.request.GET.get('tag')
            
            if cat or tag:
                tag_posts=set()
                cat_posts=set()
                if tag:
                    tag_posts=set(Tag.objects.get(slug=tag).post_set.all().prefetch_related('comment_set'))
                if cat:
                    cat_posts=set(Category.objects.get(slug=cat).post_set.all().prefetch_related('comment_set'))
                
                posts=tag_posts.union(cat_posts)
            else:
                posts=Post.objects.all().prefetch_related('comment_set')

            posts=list(posts)
            for post in posts:
                post.coment_count=post.comment_set.count()
                edit_data(post)

            return posts

        except Exception as exc:
            error_logger.error("STATUS - 500, {0}".format(exc))

            return HttpResponse(status=500)


class Blog_Item(DataMixin,DetailView):
    model=Post
    template_name='triangle/blogdetails.html'
    slug_url_kwarg='post_slug'
    context_object_name='post'
    extra_context={'title':'Blog'}
    allow_empty: False

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        try:
            context['comments']=context['post'].comment_set.all().select_related('user','answer_to')
            for comment in context['comments']:
                edit_data(comment,is_expanded=True)
                comment.answers=comment.comment_set.all().select_related('user')
                for answer in comment.answers:
                    edit_data(answer,is_expanded=True)

        except Exception as exc:
            error_logger.error("STATUS - 500, {0}".format(exc))

            return HttpResponse(status=500)

        c_def=self.get_user_context(self.request)
        context=dict(list(context.items())+list(c_def.items()))

        return context
    
    def get_object(self):
        post=Post.objects.filter(slug=self.kwargs['post_slug']).prefetch_related('comment_set','categories','tags')[:1]
        post=post[0]

        try:
            post.coment_count=post.comment_set.count()
            for category in post.categories.all():
                category.post_count=category.post_set.count()
            edit_data(post)
            return post

        except Exception as exc:
            error_logger.error("STATUS - 500, {0}".format(exc))

            return HttpResponse(status=500)


class Portfolio(DataMixin,ListView):
    model=Project
    template_name='triangle/portfolio.html'
    context_object_name='projects'
    extra_context={'title':'Portfolio'}
    allow_empty: False

    paginate_by=16

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        field_dict={
            'sections':lambda :Section.objects.all(),
        }
        cache_handler(context,field_dict)

        c_def=self.get_user_context(self.request,section_slug=self.request.GET.get('section',''))
        context=dict(list(context.items())+list(c_def.items()))

        print(context['projects'][0].photo_small)

        return context
    
    def get_queryset(self):
        try:
            projects=Project.objects.all().prefetch_related('sections')

            for project in projects:
                sect_str=''
                for section in project.sections.all():
                    sect_str+= section.slug + ' '

                project.section_str=sect_str

            return projects

        except Exception as exc:
            error_logger.error("STATUS - 500, {0}".format(exc))

            return HttpResponse(status=500)

class Portfolio_Item(DataMixin,DetailView):
    model=Post
    template_name='triangle/portfolio-details.html'
    slug_url_kwarg='project_slug'
    context_object_name='project'
    extra_context={'title':'Portfolio'}
    allow_empty: False

    def get_context_data(self,*, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        
        c_def=self.get_user_context(self.request)
        context=dict(list(context.items())+list(c_def.items()))

        return context

    def get_object(self):
        try:
            project=Project.objects.filter(slug=self.kwargs['project_slug']).prefetch_related('client','skills','projects')[:1]
            project=project[0]

            edit_data(project,is_expanded=True)

            return project
        
        except Exception as exc:
            error_logger.error("STATUS - 500, {0}".format(exc))

            return HttpResponse(status=500)

# @csrf_exempt              #* Знімає csrf захист
def add_message(request):
    if request.method=='POST':
        form=AddMessage(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None,'Помилка додавання поста')

    return redirect('home')

def add_comment(request):
    if request.GET.get('user_id')=='None':
        return redirect('login')

    if request.method=='POST':
        c_def={}

        if request.GET.get('comment_id')!='None' and request.GET.get('post_id')=='None':
            comment=Comment.objects.get(pk=int(request.GET.get('comment_id')))
            c_def['answer_to']=comment
        elif request.GET.get('post_id')!='None':
            post=Post.objects.get(pk=int(request.GET.get('post_id')))
            c_def['post']=post

        user=User.objects.get(pk=int(request.GET.get('user_id')))
        c_def['user']=user

        model_data=dict(list(request.POST.items())+list(c_def.items()))
        del model_data['submit']

        form=AddComment(model_data)
        ctx={
            'title':'Add Comment',
            'form':form,
            'comment_id':request.GET.get('comment_id'),
            'user_id':request.GET.get('user_id'),
            'post_id':request.GET.get('post_id'),
            'post':request.GET.get('post')
        }

        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None,'Помилка додавання форми')
                return render(request,'triangle/add-comment.html',context=ctx)

            return redirect('blog-item',request.GET.get('post'))
        
        # return render(request,'triangle/add-comment.html',context=ctx)
        return HttpResponse(status=500)
        
    elif request.method=='GET':
        form=AddComment()
        ctx={
            'title':'Add Comment',
            'form':form,
            'comment_id':request.GET.get('comment_id'),
            'user_id':request.GET.get('user_id'),
            'post_id':request.GET.get('post_id'),
            'post':request.GET.get('post'),
        }
        return render(request,'triangle/add-comment.html',context=ctx)

def add_response(request):
    if request.GET.get('user_id')=='None':
        return redirect('login')
    
    if request.method=='POST':

        c_def={}
        user=User.objects.get(pk=int(request.GET.get('user_id')))
        c_def['user']=user

        model_data=dict(list(request.POST.items())+list(c_def.items()))

        form=AddResponse(model_data)
        ctx={
            'title':'Add Response',
            'form':form,
            'user_id':request.GET.get('user_id')           
        }

        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None,'Помилка додавання відгука')
                return render(request,'triangle/add-response.html',context=ctx)
            
            return redirect('home')
        
        # return render(request,'triangle/add-response.html',context=ctx)
        return HttpResponse(status=500)
        
    elif request.method=='GET':
        form=AddResponse()
        ctx={
            'title':'Add Response',
            'form':form,
            'user_id':request.GET.get('user_id'),
        }
        return render(request,'triangle/add-response.html',context=ctx)

#! чомусь не проходить валідація
def add_order(request):
    if request.GET.get('user_id')=='None':
        return redirect('login')

    if request.method=='POST':
        c_def={}
        user=User.objects.get(pk=int(request.GET.get('user_id')))
        pricing=Pricing.objects.get(pk=int(request.POST['pricing']))
        c_def['pricing']=pricing
        c_def['user']=user

        model_data=dict(list(request.POST.items())+list(c_def.items()))
        del model_data['submit']
        
        form=AddOrder(model_data)
        ctx={
            'title':'Order',
            'form':form,
            'user_id':request.GET.get('user_id')
        }

        if form.is_valid():
            try:
                form.save()
                user.is_client=True
                user.save()
            except:
                form.add_error(None,'Помилка Створення замовлення')
                return render(request,'triangle/add-order.html',context=ctx)
            
            info_logger.info('user make order')
            print('make order')
            return redirect('home')

        # return render(request,'triangle/add-order.html',context=ctx)
        return HttpResponse(status=500)

    else:
        form=AddOrder()
        ctx={
            'title':'Order',
            'form':form,
            'user_id':request.GET.get('user_id')
        }

        return render(request,'triangle/add-order.html',context=ctx)


def login(request):
    if request.method=='POST':

        form=Login(request.POST)
        ctx={
            'title':'Login',
            'form':form,
            'user_id':request.session.get('user_id','None')

        }

        if form.is_valid():
            try:
                user_data=User.objects.get(email=request.POST.get('email'))
                if user_data.password == request.POST.get('password'):
                    request.session['user_id']=user_data.pk
                else:
                    raise Exception('Пароль невірний')
            except:
                info_logger.info('user doesn`t login ({0})'.format(request.POST.get('email')))

                form.add_error(None,'Помилка логінізації')
                return render(request,'triangle/login.html',context=ctx)

            info_logger.info('user login ({0})'.format(request.POST.get('email')))
            return redirect('home')

        return render(request,'triangle/login.html',context=ctx)
    else:
        form=Login()
        ctx={
            'title':'Login',
            'form':form,
            'user_id':request.session.get('user_id','None')

        }

        return render(request,'triangle/login.html',context=ctx)

def logout(request):
    is_auth_handler(request,'home')

    request.session.flush()
    return redirect('home')

def add_user(request):
    if request.method=='POST':
        if is_auth_handler(request):
            request.session.flush()

        repassword=request.POST.get('repassword')
        model_data=dict(list(request.POST.items()))
        del model_data['repassword']

        form=AddUser(model_data)
        ctx={
            'title':'Register',
            'form':form
        }

        if repassword != request.POST.get('password'):
            form.add_error(None,'Паролі не співпадають')
            return render(request,'triangle/register.html',context=ctx)
        
        if form.is_valid():
            try:
                form.save()

                user_data=User.objects.get(email=request.POST.get('email'))
                request.session['user_id']=user_data.pk
            except:
                form.add_error(None,'Помилка Створення користувача')
                return render(request,'triangle/register.html',context=ctx)

            info_logger.info('user has been created')
            return redirect('home')

    else:
        form=AddUser()
        ctx={
            'title':'Register',
            'form':form
        }

    return render(request,'triangle/register.html',context=ctx)

def page_not_fount(request,*args,**kwargs):
    return render(request,'triangle/404.html',)

def handle_error_400(request,exception):
    error_logger.error("STATUS - 400, {0}".format(exception))

    return HttpResponse(status=400)

def handle_error_403(request,exception):
    error_logger.error("STATUS - 403, {0}".format(exception))

    return HttpResponse(status=403)

def handle_error_500(request):
    error_logger.error("STATUS - 500, {0}")
    return HttpResponse(status=500)