from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404, render, HttpResponse, reverse
from django.http import HttpResponseRedirect
from django.db.models import Prefetch
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Blog, Comment, Reply
from .forms import CommentForm, ReplyForm

class BlogListView(ListView):
    queryset = Blog.objects.select_related('blog_category').filter(status='pub')
    paginate_by = 6
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Blog.objects.select_related('blog_category').filter(slug=slug)
        # return Blog.objects.select_related('blog_category').filter(slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(status='pub').values('title', 'date_creation').order_by('-date_creation')[:5]
        context['comments'] = Comment.objects.prefetch_related('replies__replies').filter(blog=self.object).all()
        context['comment_form'] = CommentForm()
        context['reply_form'] = ReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'reply_name' in self.request.POST:
            reply_form = ReplyForm(self.request.POST)
            if reply_form.is_valid():
                reply_name = reply_form.cleaned_data['reply_name']
                body = reply_form.cleaned_data['body']

                if reply_form.cleaned_data['parent_comment'] is not None:
                    parent_comment = reply_form.cleaned_data['parent_comment']
                    parent_reply = None
                else:
                    parent_comment = None
                    parent_reply = reply_form.cleaned_data['parent_reply']

                new_reply = Reply(reply_name=reply_name, body=body, blog=self.object, parent_comment=parent_comment, parent_reply=parent_reply)
                new_reply.save()
        else:
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                name = comment_form.cleaned_data['name']
                body = comment_form.cleaned_data['body']
                new_comment = Comment(name=name, body=body, blog=self.object)
                new_comment.save()

        return HttpResponseRedirect(reverse('blog_detail', args=[self.kwargs['slug']]))


