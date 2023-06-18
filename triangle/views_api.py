from .serializers import *
from .models import *
from rest_framework.viewsets import *
from rest_framework.generics import *
from .permissions import *
from rest_framework.permissions import *
from rest_framework.authentication import * 

class EmployeeViewSet(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    permission_classes=(IsAdminOrReadOnly,)

class ServiceViewSet(ModelViewSet):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

    permission_classes=(IsAdminOrReadOnly,)

class MessageViewSet(ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer

    permission_classes=(IsAdminOrReadOnlyAndCreate,)

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    permission_classes=(IsAdminUser,)

class OrderViewSet(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

    permission_classes=(IsAdminOrAuthenticatedCreate,)

class PricingViewSet(ModelViewSet):
    queryset=Pricing.objects.all()
    serializer_class=PricingSerializer

    permission_classes=(IsAdminOrReadOnly,)

class CommentViewSet(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    permission_classes=(IsAdminOrAuthenticatedCreate,)

class ResponseViewSet(ModelViewSet):
    queryset=Response.objects.all()
    serializer_class=ResponseSerializer

    permission_classes=(IsAdminOrAuthenticatedCreate)

class ProjectViewSet(ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    permission_classes=(IsAdminOrReadOnly,)

class SectionViewSet(ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer

    permission_classes=(IsAdminOrReadOnly,)

class SkillViewSet(ModelViewSet):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

    permission_classes=(IsAdminOrReadOnly,)

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    permission_classes=(IsAdminOrReadOnly,)

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    permission_classes=(IsAdminOrReadOnly,)

class TagViewSet(ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

    permission_classes=(IsAdminOrReadOnly,)