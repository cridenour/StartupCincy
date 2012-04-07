from django.views.generic import TemplateView

from startup.startups.models import Company

class HomePage(TemplateView):
    template_name = 'home.html'