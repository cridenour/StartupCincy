from django.views.generic.base import TemplateView, View
from startup.jobs.models import Job


class JobList(TemplateView):
    template_name = 'list_jobs.html'

    def get_context_data(self, **kwargs):
        jobs = Job.objects.all().order_by('-last_updated')

        return {'jobs': jobs}

