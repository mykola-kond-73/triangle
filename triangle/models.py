from operator import index
from django.db import models
from django.urls import reverse

class Employee(models.Model):
    name=models.CharField(max_length=255,verbose_name="Ім'я")
    position=models.CharField(max_length=255,verbose_name="Посада")
    photo=models.ImageField(upload_to="photos/employees/", verbose_name="Фото")
    facebook=models.CharField(max_length=255,unique=True)
    twitter=models.CharField(max_length=255,unique=True)
    email=models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Працівник'
        verbose_name_plural='Працівники'
        ordering=['name','position']

class Service(models.Model):
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")
    description=models.TextField(verbose_name='Опис')
    photo=models.ImageField(upload_to="photos/services/",verbose_name="Фото")
    is_top=models.BooleanField(default=False)
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Послуга'
        verbose_name_plural='Послуги'
        ordering=['name','time_create']

class Message(models.Model):
    statuses=[('A','accepted'),('C','considered'),('NC','not considered')]

    name=models.CharField(max_length=255,db_index=True,verbose_name="Ім'я")
    email=models.EmailField(max_length=254)
    text=models.TextField(verbose_name='Опис')
    status=models.CharField(max_length=255,choices=statuses,default='A',db_index=True,verbose_name='Статус')
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    time_update=models.DateTimeField(auto_now=True,verbose_name='Час оновлення')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Повідомлення'
        verbose_name_plural='Повідомлення'
        ordering=['name','email','status','time_create','time_update']

class User(models.Model):
    name=models.CharField(max_length=255,db_index=True,verbose_name="Ім'я")
    email=models.EmailField()
    password=models.CharField(max_length=255,verbose_name="Пароль")
    is_client=models.BooleanField(default=False,verbose_name='Чи клієнт')
    is_top=models.BooleanField(default=False)
    photo_small=models.ImageField(upload_to="photos/users/small/", verbose_name="Маленьке фото")
    photo_big=models.ImageField(upload_to="photos/users/big/", verbose_name="Велике фото")
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час Реєстрації')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Користувач'
        verbose_name_plural='Користувачі'
        ordering=['name','is_client','time_create']

class Order(models.Model):
    statuses=[
        ('A','accepted'),
        ('P','performed'),
        ('D','done'),
        ('De','denied'),
        ('ND','not done'),
    ]

    comment=models.CharField(max_length=255,verbose_name="Коментар")
    status=models.CharField(max_length=255,db_index=True,choices=statuses,default='A',verbose_name='Статус')
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    time_update=models.DateTimeField(auto_now=True,verbose_name='Час оновлення')
    time_done=models.DateTimeField(null=True,default=None,verbose_name='Час виконання')
    
    pricing=models.ForeignKey('Pricing',on_delete=models.PROTECT,null=True,verbose_name='Ціоноутворення')
    user=models.ForeignKey('User',on_delete=models.PROTECT,verbose_name='Користувач')

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name='Замовлення'
        verbose_name_plural='Замовлення'
        ordering=['status','time_create','time_update','time_done']


class Pricing(models.Model):
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")
    price=models.FloatField(verbose_name="Ціна")
    tilda=models.BooleanField()
    word_press=models.BooleanField()
    open_cart=models.BooleanField()
    custom_development=models.BooleanField()
    google_analytics=models.BooleanField()
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    time_update=models.DateTimeField(auto_now=True,verbose_name='Час оновлення')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Ціноутворення'
        verbose_name_plural='Ціноутворення'
        ordering=['name','tilda','word_press','open_cart','custom_development','google_analytics','time_create','time_update']

class Comment(models.Model):
    text=models.TextField(verbose_name='Коментар')
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    
    post=models.ForeignKey('Post',on_delete=models.CASCADE,null=True,default=None,verbose_name='Пост')
    answer_to=models.ForeignKey('Comment',on_delete=models.PROTECT,null=True,default=None,verbose_name='Відповідь на')
    user=models.ForeignKey('User',on_delete=models.PROTECT,verbose_name='Користувач')

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name='Коментар'
        verbose_name_plural='Коментарі'
        ordering=['time_create']

class Response(models.Model):
    text=models.TextField(verbose_name='Відгук')
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    
    user=models.ForeignKey('User',on_delete=models.PROTECT)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name='Відгук'
        verbose_name_plural='Відгуки'
        ordering=['time_create']

class Project(models.Model):
    slug=models.SlugField(max_length=50, unique=True,db_index=True,verbose_name='URL')
    name=models.CharField(max_length=255, unique=True,db_index=True,verbose_name="Назва")
    description=models.TextField(verbose_name='Опис')
    is_top=models.BooleanField(default=False)
    photo_small=models.ImageField(upload_to="photos/projects/small/", verbose_name="Маленьке фото")
    photo_big=models.ImageField(upload_to="photos/projects/big/", verbose_name="Велике фото")
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час публікації')
    
    client=models.ManyToManyField('User')
    skills=models.ManyToManyField('Skill')
    projects=models.ManyToManyField('Project')
    sections=models.ManyToManyField('Section')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio-item',kwargs={'project_slug':self.slug})

    class Meta:
        verbose_name='Проект'
        verbose_name_plural='Проекти'
        ordering=['name','time_create']

class Section(models.Model):
    slug=models.SlugField(max_length=50, unique=True,verbose_name='URL')
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час публікації')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Розділ'
        verbose_name_plural='Розділи'
        ordering=['name','time_create']

class Skill(models.Model):
    slug=models.SlugField(max_length=50, unique=True,verbose_name='URL')
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час публікації')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Навичка'
        verbose_name_plural='Навички'
        ordering=['name','time_create']

class Post(models.Model):
    slug=models.SlugField(max_length=50, unique=True,db_index=True,verbose_name='URL')
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")
    description=models.TextField(verbose_name='Опис')
    photo=models.ImageField(upload_to="photos/posts/", verbose_name="Фото")
    likes=models.PositiveIntegerField(default=0,verbose_name="Лайки")
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час публікації')
    
    categories=models.ManyToManyField('Category')
    tags=models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-item',kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Пости'
        ordering=['slug','name','likes','time_create']

class Category(models.Model):
    slug=models.SlugField(max_length=50, unique=True,verbose_name='URL')
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")    
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час публікації')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категорія'
        verbose_name_plural='Категорії'
        ordering=['slug','name','time_create']

class Tag(models.Model):
    slug=models.SlugField(max_length=50, unique=True,verbose_name='URL')
    name=models.CharField(max_length=255, unique=True,verbose_name="Назва")    
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час публікації')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Тег'
        verbose_name_plural='Теги'
        ordering=['slug','name','time_create']    