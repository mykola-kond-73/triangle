# Generated by Django 4.1 on 2022-08-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triangle', '0002_remove_comment_answers_comment_answer_to_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')),
            ],
            options={
                'verbose_name': 'Розділ',
                'verbose_name_plural': 'Розділи',
                'ordering': ['name', 'time_create'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')),
            ],
            options={
                'verbose_name': 'Навичка',
                'verbose_name_plural': 'Навички',
                'ordering': ['name', 'time_create'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')),
                ('client', models.ManyToManyField(to='triangle.user')),
                ('projects', models.ManyToManyField(null=True, to='triangle.project')),
                ('sections', models.ManyToManyField(to='triangle.section')),
                ('skills', models.ManyToManyField(to='triangle.skill')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекти',
                'ordering': ['name', 'time_create'],
            },
        ),
    ]