from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect

from .models import Blog, Comment
from .forms import CommentForm

class BlogList(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'

class BlogDetail(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = Comment.objects.filter(blog=self.get_object())
        number_of_comments = connected_comments.count()
        data['comments'] = connected_comments
        data['no_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()
        return data

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            print('-------------------------------------------------------------------------------Reached here')
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                name = comment_form.cleaned_data['name']
                body = comment_form.cleaned_data['body']
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent = None

                new_comment = Comment(body=body, blog=self.get_object(), parent=parent, name=name)
                new_comment.save()
            return redirect(self.request.path_info)


