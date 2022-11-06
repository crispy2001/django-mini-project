from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import Http404
from .models import Profile, User
from django.shortcuts import redirect
# from .forms import ProfileForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    

# class CreateProfile(TemplateView):
#     template_name = 'test.html'

class ProfileDetailView(DetailView):
    # toast = "variable toast"
    model = Profile
    template_name = 'profile/profile_info.html'
    
    def get_conetxt_data(self, request, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # person = get_object_or_404(Profile, pk = self.kwargs['pk'])
        try:
            person = Profile.objects.get(id = self.kwargs['pk'])
            context['person'] = person
            return context
        except Http404:
            response = redirect('home')
            return response

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetailView, self).get_context_data(**kwargs)
    #     # person = get_object_or_404(Profile, pk = self.kwargs['pk'])
    #     person = Profile.objects.get(id = self.kwargs['pk'])
    #     context['person'] = person
    #     return context

class EditProfile(UpdateView):
    model = Profile
    template_name = 'profile/profile_edit.html'

class ProfileCreateView(CreateView):
    model = Profile
    fields = ['introduction']
    template_name = 'profile.html'
    success_url = reverse_lazy('profile', kwargs = {'username': "toast"})



