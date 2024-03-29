from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin     
)
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView 
from django.urls import reverse_lazy     
from .models import Article, Comment
from .forms import CommentForm

from django.shortcuts import get_object_or_404, render, redirect 
from django.http import request, QueryDict


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    
class ArticleDetailView(DetailView): 
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView): 
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body') # new
    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

# Comment views

class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'

class CommentCreateView(LoginRequiredMixin, CreateView): 
    model = Comment
    template_name = 'comment_new.html'
    fields = ('article', 'comment',) 
    login_url = 'login'
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
