from django import forms
from .models import NComment, NReply
from django.utils.translation import gettext_lazy as _


class NCommentForm(forms.ModelForm):
    class Meta:
        model = NComment
        fields = ['name', 'body']
        widgets = {'body': forms.TextInput()}

class NReplyForm(forms.ModelForm):
    class Meta:
        model = NReply
        fields = ['reply_name', 'body', 'parent_comment', 'parent_reply']
        widgets = {'body': forms.TextInput()}

