from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import Http404, request, response
from .models import Article, User
from clubs.models import Club
from .forms import ArticleForm
from django.shortcuts import redirect, reverse
import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin

class ArticleDetailView(UserPassesTestMixin, TemplateView):
    def test_func(self):
        article = Article.objects.get( id = self.kwargs['pk'])
        if article.user_id == self.request.user.id or article.is_visable == 1:
            return self.request.user
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
        return reverse('profile', kwargs = {'pk': self.request.user.id})


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

        # check the view permission
        x= self.request.POST.get('is_visable')
        if x == "on":
            form.instance.is_visable = 1
        else:
            form.instance.is_visable = 0
        print(form.instance.is_visable)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article', kwargs = {'pk': self.kwargs['pk']})


####################
# club
####################

class ClubArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'article/club_article_create.html'
    print("club article create view")
    def form_valid(self, form):
        print("club article create viewWWWWWWWWW")
        form.instance.user_id = self.request.user.id
        form.instance.create_time = datetime.datetime.now()
        form.instance.club_id = self.kwargs['club_pk']
        print(datetime.datetime.now())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('club', kwargs = {'pk': self.kwargs['club_pk']})


class ClubArticleUpdateView(UserPassesTestMixin, UpdateView):
    
    def test_func(self):
        article = Article.objects.get( id = self.kwargs['pk'])
        if article.user_id == self.request.user.id:
            return self.request.user

    form_class = ArticleForm
    template_name = 'article/club_article_update.html'

    def get_queryset(self, **kwargs):
        return Article.objects.filter(id = self.kwargs['pk'] )

    def get_context_data(self, **kwargs):
        context = super(ClubArticleUpdateView, self).get_context_data(**kwargs)
        article = Article.objects.get(id = self.kwargs['pk'])
        context['article'] = article
        return context

    def form_valid(self, form):
        form.instance.update_time = datetime.datetime.now()

        # check the view permission
        x= self.request.POST.get('is_visable')
        if x == "on":
            form.instance.is_visable = 1
        else:
            form.instance.is_visable = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('club-article', kwargs = {'club_pk': self.kwargs['club_pk'], 'pk': self.kwargs['pk']})
    
class ClubArticleDetailView(UserPassesTestMixin, TemplateView):
    def test_func(self):
        # article = Article.objects.get( id = self.kwargs['pk'])
        # if article.user_id == self.request.user.id or article.is_visable == 1:
        
        # if Club.objects.filter(user__id = self.request.user.id):
        #     return self.request.user
        u = User.objects.get( id = self.request.user.id)
        clubs_joined = u.club_set.all()
        try:
            club = clubs_joined.get(id = self.kwargs['club_pk'])
            return self.request.user
        except:
            print("doesnt exist")

    model = Article
    template_name = 'article/club_article.html'
    
    def get_context_data(self, **kwargs):
        context = super(ClubArticleDetailView, self).get_context_data(**kwargs)
        article = Article.objects.get(id = self.kwargs['pk'])
        context['article'] = article
        return context
