from django.urls import path
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('add-message/',add_message,name='add-message'),
    path('add-response/',add_response,name='add-response'),

    path('about/',Aboutus.as_view(),name='about'),
    path('services/',Sercices.as_view(),name='services'),
    path('pricing/',Pricings.as_view(),name='pricing'),
    path('contacts/',Contacts.as_view(),name='contacts'),

    path('blog/',Blog.as_view(),name='blog'),
    path('blog/<slug:post_slug>',Blog_Item.as_view(),name='blog-item'),
    path('add-comment/',add_comment,name='add-comment'),


    path('portfolio/',Portfolio.as_view(),name='portfolio'),
    path('portfolio/<slug:project_slug>',Portfolio_Item.as_view(),name='portfolio-item'),

    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('add-user/',add_user,name='add-user'),
    
    path('order/',add_order,name='order')
]