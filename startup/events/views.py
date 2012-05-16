from django.views.generic import View, TemplateView
from django.shortcuts import HttpResponse
from django.utils.html import strip_tags
from datetime import datetime
from startup.events.models import Event, MeetupGroups
from startup.events.utils import meetup_api_request

class EventsListing(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        featured_raw = Event.objects.filter(start__gte=datetime.now(), approved=True, featured=True).order_by('start')[0:3]
        upcoming_raw = Event.objects.filter(start__gte=datetime.now(), approved=True, featured=False).order_by('start')[0:4]

        featured = []
        for f in featured_raw:
            featured.append(
                {
                    'id': f.id,
                    'title': f.title,
                    'description': strip_tags(f.description),
                    'who': f.who,
                    'where': f.where,
                    'month': f.start.strftime('%b'),
                    'day': f.start.strftime('%d'),
                    'time': f.start.strftime('%I:%M%p'),
                    'active': True if len(featured) is 0 else False,
                    'link' : f.link,
                    'color': self.next_color(),
                }
            )

        upcoming = []
        clear = False
        for u in upcoming_raw:
            upcoming.append(
                {
                'id': u.id,
                'title': u.title,
                'description': strip_tags(u.description),
                'who': u.who,
                'where': u.where,
                'month': u.start.strftime('%b'),
                'day': u.start.strftime('%d'),
                'time': u.start.strftime('%I:%M%p'),
                'link' : u.link,
                'clear': clear
                }
            )

            clear = not clear

        return {'featured': featured, 'upcoming': upcoming}

    COLORS = ['blue', 'red', 'orange']
    COLOR_INDEX = 0

    def next_color(self):
        ret = self.COLORS[self.COLOR_INDEX]
        if self.COLOR_INDEX < 2:
            self.COLOR_INDEX += 1
        else:
            self.COLOR_INDEX = 0

        return ret

class FindNewEvents(View):
    def get(self, request, *args, **kwargs):

        # Meetup API
        groups = MeetupGroups.objects.filter(enabled=True)
        for g in groups:
            response = meetup_api_request('events?sign=true&time=1d,2m&group_id=' + str(g.meetup_id))

            if response.get('meta', {}).get('count', 0) > 0:
                events = response.get('results')

                for e in events:
                    existing = Event.objects.filter(meetup_id=e.get('id'))
                    if len(existing) > 0:
                        continue

                    event = Event()
                    event.title = e.get('name')
                    event.description = e.get('description')
                    event.start = datetime.fromtimestamp(float(e.get('time')) / 1000)
                    event.where = ', '.join([e.get('venue').get('name'), e.get('venue').get('address_1'), e.get('venue').get('zip')]) if e.get('venue') else 'No Location'
                    event.who = e.get('group').get('name')
                    event.meetup_id = e.get('id')
                    event.link = e.get('event_url')

                    if g.auto_post:
                        event.approved = True
                    if g.auto_feature:
                        event.featured = True

                    event.save()
            else:
                continue

        return HttpResponse(status=200)