from django import forms
from .models import Message,Comment,Response,Order,User
from captcha.fields import CaptchaField

class AddMessage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddMessage, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model=Message
        fields=['name','email','text']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':"Name",'type':"text",'name':"name"}),
            'email':forms.TextInput(attrs={'placeholder':'Email Id','type':"email",'name':"email"}),
            'text':forms.Textarea(attrs={'rows':'8','placeholder':"Your text here",'name':"text",'id':"message"})
        }
        labels=None
        # error_messages={}

class AddComment(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['post'].required=False
        self.fields['answer_to'].required=False

    class Meta:
        model=Comment
        fields=['text','user','post','answer_to']
        widgets={}
        labels={'text':'Your text here'}
        # error_messages={}

class AddResponse(forms.ModelForm):
    class Meta:
        model=Response
        fields=['text','user']
        widgets={}
        labels={'text':'Your text here'}
        # error_messages={}

class AddOrder(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['pricing'].empty_label='Pricings'
        self.fields['user'].required=False
        self.fields['captcha']=CaptchaField()

    class Meta:
        model=Order
        fields=['comment','pricing','user']
        widgets={}
        labels={
            'comment':'Your text here',
            'pricing':'Your pricing'
        }
        # error_messages={}

class AddUser(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['photo_small'].required=False
        self.fields['photo_big'].required=False
        self.fields['repassword']=forms.CharField(max_length=255)
        self.fields['repassword'].widget=forms.TextInput(attrs={'placeholder':"Replay Your Password",'type':"password",'name':"repassword"})
        self.fields['repassword'].label='Replay Your password'
        self.fields['repassword'].required=False
        self.fields['captcha']=CaptchaField()


    class Meta:
        model=User
        fields=['name','email','photo_small','photo_big','password']
        widgets={
            'password':forms.TextInput(attrs={'placeholder':"Password",'type':"password",'name':"password"}),
            'email':forms.TextInput(attrs={'placeholder':'Email Id','type':"email",'name':"email"}),
            'name':forms.TextInput(attrs={'placeholder':"Name",'type':"text",'name':"name"}),
        }
        labels={
            'name':'Your Name',
            'email':'Your E-mail',
            'photo_small':'Add your small photo',
            'photo_big':'Add your big photo',
            'password':'Your password',
        }
        # error_messages={}



class Login(forms.Form):
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email Id','type':"email",'name':"email"}))   
    password=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':"Password",'type':"password",'name':"password"})) 
    captcha=CaptchaField()
