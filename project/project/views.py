from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'allauth.html'

class Test(TemplateView):
    template_name = 'test.html'