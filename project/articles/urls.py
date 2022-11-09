from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    re_path(r'create', views.ArticleCreateView.as_view(), name = 'create-article'),
    re_path(r'^(?P<pk>\w+)/update', views.ArticleUpdateView.as_view(), name = 'update-article'),
    re_path(r'^(?P<pk>\w+)', views.ArticleDetailView.as_view(), name = 'article'),
]
