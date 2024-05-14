from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Blog(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=300, null=True)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    published_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(default='a user', max_length=40)
    body = models.TextField()
    published_date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_date_time']

    def __str__(self):
        return str(self.name) + ':' + str(self.body)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


