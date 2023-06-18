from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from coolsite import settings
from triangle.views import page_not_fount,handle_error_403,handle_error_400,handle_error_500
from rest_framework import routers
from triangle.views_api import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router=routers.DefaultRouter()
router.register(r'employee',EmployeeViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'message',MessageViewSet)
router.register(r'user', UserViewSet)
router.register(r'order',OrderViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'response',ResponseViewSet)
router.register(r'project',ProjectViewSet)
router.register(r'section', SectionViewSet)
router.register(r'skill',SkillViewSet)
router.register(r'post',PostViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'tag',TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('triangle.urls')),
    path('captcha/', include('captcha.urls')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/',include(router.urls)),    
]

if settings.DEBUG:
    import debug_toolbar
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns=[
        path('__debug__/', include('debug_toolbar.urls'))

    ] + urlpatterns
    
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404=page_not_fount
handler500=handle_error_500
handler403=handle_error_403
handler400=handle_error_400