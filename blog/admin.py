from django.contrib import admin
from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'slug', 'published_date_time')
    ordering = ('-published_date_time', )
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'body', 'published_date_time')
    ordering = ('-published_date_time',)

