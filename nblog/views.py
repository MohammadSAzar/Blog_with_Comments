from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponseRedirect

from .models import NBlog, NComment, NReply
from .forms import NCommentForm, NReplyForm


class NBlogListView(ListView):
    queryset = NBlog.objects.all()
    context_object_name = 'nblogs'
    template_name = 'nblog/nblog_list.html'


class NBlogDetailView(DetailView):
    template_name = 'nblog/nblog_detail.html'
    model = NBlog

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments = NComment.objects.filter(post=self.get_object())
        replies = NReply.objects.filter(post=self.get_object())
        number_of_comments_and_replies = comments.count() + replies.count()
        data['comments'] = comments
        data['replies'] = replies
        data['number_of_comments_and_replies'] = number_of_comments_and_replies
        data['comment_form'] = NCommentForm()
        data['reply_form'] = NReplyForm()
        return data

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            if 'reply_name' in self.request.POST:
                reply_form = NReplyForm(self.request.POST)
                print('PUSSSSSSSSSSSSSSSSSS')
                if reply_form.is_valid():
                    reply_name = reply_form.cleaned_data['reply_name']
                    body = reply_form.cleaned_data['body']

                    if reply_form.cleaned_data['parent_comment'] is not None:
                        parent_comment = reply_form.cleaned_data['parent_comment']
                        print('GOH')
                        parent_reply = None
                    else:
                        parent_comment = None
                        print('AN')
                        parent_reply = reply_form.cleaned_data['parent_reply']

                    new_reply = NReply(reply_name=reply_name, body=body, post=self.get_object(), parent_comment=parent_comment, parent_reply=parent_reply)
                    new_reply.save()
            else:
                comment_form = NCommentForm(self.request.POST)
                print('ASSSSSSSSSSSSSSSS')
                if comment_form.is_valid():
                    name = comment_form.cleaned_data['name']
                    body = comment_form.cleaned_data['body']
                    new_comment = NComment(name=name, body=body, post=self.get_object())
                    new_comment.save()

            # return reverse(self.object.get_absolute_url())
            return HttpResponseRedirect(reverse('nblog_list'))

    # def post(self, request, *args, **kwargs):
    #     if self.request.method == 'POST':
    #         print('-------------------------------------------------------------------------------Reached here')
    #         comment_form = NCommentForm(self.request.POST)
    #         reply_form = NReplyForm(self.request.POST)
    #         if comment_form.is_valid():
    #             name = comment_form.cleaned_data['name']
    #             body = comment_form.cleaned_data['body']
    #             new_comment = NComment(name=name, body=body, post=self.get_object())
    #             new_comment.save()
    #
    #         if reply_form.is_valid():
    #             name = reply_form.cleaned_data['name']
    #             body = reply_form.cleaned_data['body']
    #             level = request.POST.get('level', False)
    #             if level == 1:
    #                 parent_comment = request.POST.get('parent_comment', False)
    #                 parent_reply = None
    #             else:
    #                 parent_comment = None
    #                 # parent_reply = request.POST.get('parent_reply', False)
    #             level += level
    #             new_reply = NReply(name=name, body=body, post=self.get_object(), parent_comment=parent_comment)
    #             new_reply.save()
    #
    #         # return reverse(self.object.get_absolute_url())
    #         return HttpResponseRedirect(reverse('nblog_list'))

