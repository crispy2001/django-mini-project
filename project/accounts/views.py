from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import Http404, request, response
from .models import Profile, User
from articles.models import Article
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('allauth')
    template_name = 'signup.html'

class ProfileIndexView(TemplateView):
    # model = Profile
    template_name = 'profile/profile_info.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileIndexView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(id = self.kwargs['pk'])
        person = User.objects.get(id = self.kwargs['pk'])
    
        if profile.id == self.request.user.id:
            articles = Article.objects.filter(user_id = self.request.user.id)
            context['articles'] = articles
        else:
            articles = Article.objects.get(user_id = profile.id, is_visable = 1)
            context['articles'] = articles
        context['profile'] = profile
        context['person'] = person
        return context


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        profile = Profile.objects.get( id = self.kwargs['pk'])
        if profile.id == self.request.user.id:
            return self.request.user

    form_class = ProfileForm
    template_name = 'profile/profile_update.html'
    
    def get_queryset(self, **kwargs):
        return Profile.objects.filter(user = self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(id = self.kwargs['pk'])
        context['profile'] = profile
        return context
        
    def get_success_url(self):
        return reverse('profile', kwargs = {'pk': self.kwargs['pk']})





