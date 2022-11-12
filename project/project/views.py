from django.contrib.auth.models import User
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'allauth.html'

class Test(TemplateView):
    template_name = 'test.html'
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        users = User.objects.filter()
        print(users)
        context['users'] = users
        return context
