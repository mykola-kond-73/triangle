from turtle import position
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','email','position','photo','get_html_photo','facebook','twitter')
    list_display_links=('name','email')
    search_fields=('name','position')
    list_filter=('position',)
    ordering=('id',)
        
    fields=('name','email','position','photo','facebook','twitter')
    readonly_fields=('id',)

    actions_on_bottom=True
    list_per_page: 10

    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_description='Фото'

class ServiceAdmin(admin.ModelAdmin):
    list_display=('id','name','description','photo','get_html_photo','is_top','time_create')
    list_display_links=('name',)
    search_fields=('name','description')
    list_filter=('is_top','time_create')
    list_editable=('is_top',)
    ordering=('id',)

    fields=('id','name','description','photo','is_top','time_create')
    readonly_fields=('id','time_create',)

    actions_on_bottom=True
    list_per_page: 10

    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_decription='Фото'

class MessageAdmin(admin.ModelAdmin):
    list_display=('id','name','email','text','status','time_create','time_update')
    list_display_links=None
    search_fields=('name','email')
    list_filter=('status','time_create','time_update')
    list_editable=('status',)
    ordering=('id',)

    actions_on_bottom=True
    list_per_page: 10

class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password','is_client','is_top','photo_small','get_html_photo_small','photo_big','get_html_photo_big','time_create')
    list_display_links=None
    ordering=('id',)
    search_fields=('name','email')
    list_filter=('is_client','is_top','time_create')
    list_editable=('is_client','is_top')
    

    fields=('id','name','email','password','is_client','is_top','photo_small','photo_big','time_create')
    readonly_fields=('id','time_create')

    actions_on_bottom=True
    list_per_page: 10

    def get_html_photo_small(self,object):
        if object.photo_small:
            return mark_safe(f"<img src='{object.photo_small.url}' width=50>")

    def get_html_photo_big(self,object):
        if object.photo_big:
            return mark_safe(f"<img src='{object.photo_big.url}' width=50>")

    get_html_photo_small.short_description='Маленьке Фото'
    get_html_photo_big.short_description='Велике Фото'

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','comment','status','time_create','time_update','time_done','pricing','pricing_id','user','user_id')
    list_display_links=('id','comment')
    ordering=('id',)
    list_filter=('status','time_create','time_update','time_done','pricing')
    list_editable=('status','pricing','user')

    fields=('id','status','time_create','time_update','time_done','pricing','user')
#! щось придумати із 'time_done'
    readonly_fields=('id','time_create','time_update','time_done')

    actions_on_bottom=True
    list_per_page: 10

class PricingAdmin(admin.ModelAdmin):
    list_display=('id','name','price','tilda','word_press','open_cart','custom_development','google_analytics','time_create','time_update')
    list_display_links=('name',)
    ordering=('id',)
    search_fields=('name','price')
    list_filter=('tilda','word_press','open_cart','custom_development','google_analytics','time_create','time_update')
    list_editable=('tilda','word_press','open_cart','custom_development','google_analytics')

    fields=('id','name','price','tilda','word_press','open_cart','custom_development','google_analytics','time_create','time_update')
    readonly_fields=('id','time_create','time_update')

    actions_on_bottom=True
    list_per_page: 10

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','text','time_create','post','post_id','answer_to','user','user_id')
    list_display_links=None
    ordering=('id',)
    list_filter=('time_create',)

    actions_on_bottom=True
    list_per_page: 10

class ResponseAdmin(admin.ModelAdmin):
    list_display=('id','text','time_create','user','user_id')
    list_display_links=None
    ordering=('id',)
    list_filter=('time_create',)

    actions_on_bottom=True
    list_per_page: 10

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','slug','name','description','is_top','photo_small','get_html_photo_small','photo_big','get_html_photo_big','time_create','get_clients','get_skills','get_sections','get_projects')
    list_display_links=('slug','name')
    ordering=('id',)
    search_fields=('name','slug','description')
    list_filter=('is_top','time_create')
    list_editable=('is_top',)
    prepopulated_fields={'slug':('name',)}
    
    filter_horizontal = ('client','skills','projects','sections')

    fields=('id','slug','name','description','is_top','photo_small','get_html_photo_small','photo_big','get_html_photo_big','time_create','client','skills','projects','sections')
    readonly_fields=('id','time_create','get_html_photo_small','get_html_photo_big')
  
    actions_on_bottom=True
    list_per_page: 10

    def get_html_photo_small(self,object):
        if object.photo_small:
            return mark_safe(f"<img src='{object.photo_small.url}' width=50>")

    def get_html_photo_big(self,object):
        if object.photo_big:
            return mark_safe(f"<img src='{object.photo_big.url}' width=50>")

    def get_clients(self,object):
        return "\n".join([c.name+ " | " for c in object.client.all()])

    def get_skills(self,object):
        return "\n".join([c.name+ " | " for c in object.skills.all()])

    def get_sections(self,object):
        return "\n".join([c.name+ " | " for c in object.sections.all()])
    
    def get_projects(self,object):
        return "\n".join([c.name + " | " for c in object.projects.all()])

    get_html_photo_small.short_description='Маленьке Фото'
    get_html_photo_big.short_description='Велике Фото'
    get_clients.short_description='Клієнти'
    get_skills.short_description='Здібності'
    get_sections.short_description='Секції'
    get_projects.short_description='Проекти'

class SectionAdmin(admin.ModelAdmin):
    list_display=('id','slug','name','time_create')
    list_display_links=('slug','name')
    ordering=('id',)
    search_fields=('slug','name')
    list_filter=('slug','time_create')

    fields=('id','slug','name','time_create')
    readonly_fields=('id','time_create')

    actions_on_bottom=True
    list_per_page: 10

class SkillAdmin(admin.ModelAdmin):
    list_display=('id','slug','name','time_create')
    list_display_links=('slug','name')
    ordering=('id',)
    search_fields=('slug','name')
    list_filter=('slug','time_create')

    fields=('id','slug','name','time_create')
    readonly_fields=('id','time_create')

    actions_on_bottom=True
    list_per_page: 10    

class PostAdmin(admin.ModelAdmin):
    list_display=('id','slug','name','description','photo','get_html_photo','likes','time_create','get_categories','get_tags')
    list_display_links=('slug','name')
    ordering=('id',)
    search_fields=('slug','name','description')
    list_filter=('time_create',)
    prepopulated_fields={'slug':('name',)}

    filter_horizontal = ('categories','tags')

    fields=('id','slug','name','description','photo','get_html_photo','likes','time_create','categories','tags')
    readonly_fields=('id','time_create','get_html_photo')

    actions_on_bottom=True
    list_per_page: 10

    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    
    def get_categories(self,object):
        return "\n".join([c.name+ " | " for c in object.categories.all()])

    def get_tags(self,object):
        return "\n".join([c.name+ " | " for c in object.tags.all()])

    get_html_photo.short_description='Фото'
    get_categories.short_description='Категорія'
    get_tags.short_description='Теги'

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','slug','name','time_create')
    list_display_links=('slug','name')
    ordering=('id',)
    search_fields=('slug','name')
    list_filter=('time_create',)

    fields=('id','slug','name','time_create')
    readonly_fields=('id','time_create')

    actions_on_bottom=True
    list_per_page: 10

class TagAdmin(admin.ModelAdmin):
    list_display=('id','slug','name','time_create')
    list_display_links=('slug','name')
    ordering=('id',)
    search_fields=('slug','name')
    list_filter=('time_create',)

    fields=('id','slug','name','time_create')
    readonly_fields=('id','time_create')

    actions_on_bottom=True
    list_per_page: 10

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Pricing,PricingAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Response,ResponseAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Section,SectionAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)

admin.site.site_header=''
admin.site.site_title=''