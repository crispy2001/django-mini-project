from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    re_path(r'create', views.ClubCreateView.as_view(), name = 'club-create'),
    # re_path(r'^(?P<pk>\w+)/update', views.ClubUpdateView.as_view(), name = 'club-update'),
    re_path(r'^(?P<pk>\w+)', views.ClubDetailView.as_view(), name = 'club'),
    # re_path(r'', views.ClubIndexView.as_view(), name = 'club-index'),
]
