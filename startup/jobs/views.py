from django.shortcuts import render_to_response, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View
from jobs.models import Job, EmployerProfile
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.utils.text import truncate_html_words
import json


class JobList(TemplateView):
    template_name = 'list_jobs.html'

    def get_context_data(self, **kwargs):
        jobs = Job.objects.values('id', 'title', 'company', 'location', 'experience', 'description').order_by('-post_date')[:10]
        jobs_data = []
        for j in jobs:
            j["minExp"] = j["experience"].split(',')[0]
            j["maxExp"] = max(j["experience"].split(','))
            j["teaser"] = truncate_html_words(j["description"], 18)
            jobs_data.append(j)

        data = json.dumps(jobs_data)



        locations = Job.objects.values('location').distinct()
        location_data = ['- Select a Location -']
        for l in locations:
            location_data.append(l["location"])

        return {'data': data, 'locations': location_data}

    def post(self, request):
        # TODO: Pagination
        context = self.get_context_data()
        return HttpResponse(context["data"], mimetype='application/json')

    def dispatch(self, *args, **kwargs):
        return super(JobList, self).dispatch(*args, **kwargs)

