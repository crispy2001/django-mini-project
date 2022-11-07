from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import Http404, request, response
from .models import Profile, User
from django.shortcuts import redirect, reverse

from .forms import ProfileForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('allauth')
    template_name = 'signup.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_info.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        person = Profile.objects.get(id = self.kwargs['pk'])
        context['person'] = person
        return context


class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    template_name = 'profile/profile_update.html'
    
    def get_queryset(self, **kwargs):
        return Profile.objects.filter(user = self.request.user.id)
        #我先處理好別的問題，可不可以修改他人權限的東西先放著，目前的狀態是只能修改自己的profile，如果url輸入別人的update profile會直接噴錯
        
        # if self.request.user.is_authenticated():
        #     return Profile.objects.filter(user = self.kwargs['pk'])
        
        # else:
        #     return queryset.filter(pk = self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(id = self.kwargs['pk'])
        context['profile'] = profile
        return context
        
    def get_success_url(self):
        return reverse('profile', kwargs = {'pk': self.kwargs['pk']})





