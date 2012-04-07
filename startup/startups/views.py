from django.views.generic import TemplateView

from startup.startups.models import Company

class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        companies = Company.objects.all()[0:3]

        return {'companies': companies}