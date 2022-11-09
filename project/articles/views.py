from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import Http404, request, response
from .models import Article
from .forms import ArticleForm
from django.shortcuts import redirect, reverse
import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        article = Article.objects.get(id = self.kwargs['pk'])
        context['article'] = article
        return context

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'article/article_create.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.create_time = datetime.datetime.now()
        print(datetime.datetime.now())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article', kwargs = {'pk': self.kwargs['pk']})


class ArticleUpdateView(UserPassesTestMixin, UpdateView):
    
    def test_func(self):
        article = Article.objects.get( id = self.kwargs['pk'])
        if article.user_id == self.request.user.id:
            return self.request.user

    form_class = ArticleForm
    template_name = 'article/article_update.html'

    def get_queryset(self, **kwargs):
        return Article.objects.filter(id = self.kwargs['pk'] )

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        article = Article.objects.get(id = self.kwargs['pk'])
        context['article'] = article
        return context

    def form_valid(self, form):
        form.instance.update_time = datetime.datetime.now()
        print(datetime.datetime.now())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article', kwargs = {'pk': self.kwargs['pk']})

    

