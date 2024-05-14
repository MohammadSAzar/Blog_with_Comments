from django.contrib import admin
from .models import NBlog, NComment, NReply


@admin.register(NBlog)
class NBlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'body', 'slug', 'created_time')
	ordering = ('-created_time',)
	prepopulated_fields = {'slug': ('title',)}


@admin.register(NComment)
class NCommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'name', 'body', 'created_time')
	ordering = ('-created_time',)


@admin.register(NReply)
class NReplyAdmin(admin.ModelAdmin):
	list_display = ('reply_name', 'body', 'parent_comment', 'parent_reply', 'level', 'created_time')
	ordering = ('-created_time',)
