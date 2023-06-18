from dataclasses import field
from rest_framework.serializers import *
from .models import *

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class ServiceSerializer(ModelSerializer):
    class Meta:
        model=Service
        fields='__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        exclude=('password',)

class UserSerializerForAnotherSerializers(ModelSerializer):
    class Meta:
        model=User
        fields=('name','photo_small','photo_big')

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        depth=1

class PricingSerializer(ModelSerializer):
    class Meta:
        model=Pricing
        fields='__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=('text','time_create','post','answer_to','user')
        depth=1
    
    user=UserSerializerForAnotherSerializers(read_only=True)

class ResponseSerializer(ModelSerializer):
    class Meta:
        model=Response
        fields=('text','time_create','user')
        depth=1

    user=UserSerializerForAnotherSerializers(read_only=True)


class ProjectSerializer(ModelSerializer):
    class Meta:
        model=Project
        fields=('slug','name','description','is_top','photo_small','photo_big','time_create','skills','projects','sections','client')
        depth=1

    client=UserSerializerForAnotherSerializers(many=True,read_only=True)


class SectionSerializer(ModelSerializer):
    class Meta:
        model=Section
        fields='__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'

class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        depth=1

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class TagSerializer(ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'