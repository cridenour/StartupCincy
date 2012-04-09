from django.views.generic.base import TemplateView
from django.shortcuts import Http404
from startup.jobs.models import Job


class JobList(TemplateView):
    template_name = 'list_jobs.html'

    def get_context_data(self, **kwargs):
        jobs = Job.objects.all().order_by('-last_updated')

        return {'jobs': jobs}

class JobDetail(TemplateView):
    template_name = 'job_detail.html'

    def get_context_data(self, **kwargs):
        try:
            job = Job.objects.get(id=kwargs.get('id'))

            return {'job': job}
        except:
            raise Http404