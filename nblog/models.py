from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
import uuid


class NBlog(models.Model):
	title = models.CharField(max_length=200, unique=True)
	description = models.CharField(max_length=300, null=True)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	created_time = models.DateTimeField(auto_now_add=True)
	# id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return str(self.title)

	class Meta:
		ordering = ['-created_time']

	def get_absolute_url(self):
		return reverse('nblog_detail', args=[self.slug])


class NComment(models.Model):
	name = models.CharField(default='user1', max_length=40)
	post = models.ForeignKey(NBlog, on_delete=models.CASCADE, related_name='comments')
	body = models.CharField(max_length=150)
	created_time = models.DateTimeField(auto_now_add=True)
	# id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return f'{self.name} : {self.body[:30]}'

	class Meta:
		ordering = ['-created_time']


class NReply(models.Model):
	reply_name = models.CharField(default='a user', max_length=40)
	post = models.ForeignKey(NBlog, on_delete=models.CASCADE, related_name='whole_replies', blank=True, null=True)
	parent_comment = models.ForeignKey(NComment, on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
	parent_reply = models.ForeignKey('NReply', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
	level = models.IntegerField(default=1)
	body = models.CharField(max_length=150)
	created_time = models.DateTimeField(auto_now_add=True)
	# id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return f'{self.reply_name} : {self.body[:30]}'

	class Meta:
		ordering = ['created_time']
