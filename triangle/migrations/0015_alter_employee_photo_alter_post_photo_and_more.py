# Generated by Django 4.1 on 2022-09-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triangle', '0014_alter_employee_photo_alter_post_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='photos/employees/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='photos/posts/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo_big',
            field=models.ImageField(upload_to='photos/projects/big/', verbose_name='Велике фото'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo_small',
            field=models.ImageField(upload_to='photos/projects/small/', verbose_name='Маленьке фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(upload_to='photos/services/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_big',
            field=models.ImageField(upload_to='photos/users/big/', verbose_name='Велике фото'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_small',
            field=models.ImageField(upload_to='photos/users/small/', verbose_name='Маленьке фото'),
        ),
    ]