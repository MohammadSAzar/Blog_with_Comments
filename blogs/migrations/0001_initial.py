# Generated by Django 5.0.6 on 2024-05-17 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Blog title')),
                ('body', models.TextField(verbose_name='Blog body')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Datetime of creation')),
                ('date_modification', models.DateField(auto_now=True, verbose_name='Datetime of modification')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
                ('status', models.CharField(choices=[('pub', 'Published'), ('drf', 'Draft')], max_length=3, verbose_name='Blog status')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_category', to='blogs.blogcategory', verbose_name='Blog category')),
            ],
            options={
                'ordering': ('-date_creation',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Comment Name')),
                ('body', models.CharField(max_length=500, verbose_name='Comment Text')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.blog')),
            ],
            options={
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_name', models.CharField(max_length=40, verbose_name='Reply Name')),
                ('body', models.CharField(max_length=500, verbose_name='Reply Text')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_replies', to='blogs.blog')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blogs.comment')),
                ('parent_reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blogs.reply')),
            ],
            options={
                'ordering': ['date_creation'],
            },
        ),
    ]
