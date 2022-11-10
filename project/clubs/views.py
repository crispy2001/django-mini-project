from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import Http404, request, response
from .models import Club, User
from .forms import ClubForm
from django.shortcuts import redirect, reverse
import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin

class ClubIndexView(TemplateView):
    template_name = 'club/club_index.html'

    def get_context_data(self, **kwargs):
        context = super(ClubDetailView, self).get_context_data(**kwargs)
        club = Club.objects.get(id = self.kwargs['pk'])
        context['club'] = club
        return context


class ClubDetailView(UserPassesTestMixin, TemplateView):
    def test_func(self):
        club = Club.objects.get( id = self.kwargs['pk'])
        # print(club.user.all()[0].id)
        # test = Club.objects.filter(user__id = self.request.user.id)
        if  Club.objects.filter(user__id = self.request.user.id):
            return self.request.user
    
    model = Club
    template_name = 'club/club_info.html'
    
    def get_context_data(self, **kwargs):
        context = super(ClubDetailView, self).get_context_data(**kwargs)
        club = Club.objects.filter(id = self.kwargs['pk'])[0]
        members = Club.objects.get( id = self.kwargs['pk']).user.all().filter()

        context['club'] = club
        context['members'] = members
        return context

class ClubCreateView(CreateView):
    form_class = ClubForm
    template_name = 'club/club_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.admin_id = self.request.user.id
        instance.save()
        form.save_m2m()
        instance.user.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self, form):
        return reverse('club', kwargs = {'pk': self.object.pk})


class ClubUpdateView(UserPassesTestMixin, UpdateView):
    
    def test_func(self):
        club = Club.objects.get( id = self.kwargs['pk'])
        if club.user_id == self.request.user.id:
            return self.request.user

    form_class = ClubForm
    template_name = 'club/club_update.html'

    def get_queryset(self, **kwargs):
        return Club.objects.filter(id = self.kwargs['pk'] )

    def get_context_data(self, **kwargs):
        context = super(ClubUpdateView, self).get_context_data(**kwargs)
        club = Club.objects.get(id = self.kwargs['pk'])
        context['club'] = club
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
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('club', kwargs = {'pk': self.kwargs['pk']})

    

