from django.views.generic import TemplateView
from django.shortcuts import Http404
from startup.startups.models import Company

class HomePage(TemplateView):
    template_name = 'home.html'

class Startups(TemplateView):
    template_name = 'list_companies.html'

    def get_context_data(self, **kwargs):
        startups = Company.objects.all().order_by('-founded')

        return {'startups': startups}

class Startup(TemplateView):
    template_name = 'company_detail.html'

    def get_context_data(self, **kwargs):
        perma = kwargs.get('permalink')

        comps = Company.objects.filter(permalink=perma)
        if len(comps) > 0:
            comp = comps[0]

            return {'startup': comp, 'people': comp.people.all() }
        else:
            raise Http404