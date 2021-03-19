from django.contrib.auth import user_logged_in
from django import forms
from .models import Article, Comment


class CommentForm(forms.Form):
    model = Comment
    commment = forms.CharField(widget=forms.Textarea())
