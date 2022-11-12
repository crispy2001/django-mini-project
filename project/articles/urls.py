from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    re_path(r'^club/(?P<club_pk>\w+)/create', views.ClubArticleCreateView.as_view(), name = 'club-article-create'),
    re_path(r'^club/(?P<club_pk>\w+)/(?P<pk>\w+)/update', views.ClubArticleUpdateView.as_view(), name = 'club-article-update'),
    re_path(r'^club/(?P<club_pk>\w+)/(?P<pk>\w+)', views.ClubArticleDetailView.as_view(), name = 'club-article'),

    re_path(r'create', views.ArticleCreateView.as_view(), name = 'article-create'),
    re_path(r'^(?P<pk>\w+)/update', views.ArticleUpdateView.as_view(), name = 'article-update'),
    re_path(r'^(?P<pk>\w+)', views.ArticleDetailView.as_view(), name = 'article'),

    # re_path(r'club/^(?P<pk>\w+)', TemplateView.as_view(template_name='test.html')),

]
