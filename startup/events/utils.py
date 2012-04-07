import re
import json
import requests

MEETUP_API_KEY = '151b321b2a7841332d3371351a2e37'

def get_meetup_group_id(url):
    regex_str = 'com/(.+)/'
    r = re.search(regex_str, url)
    if r.group(1) is None:
        return False

    api_response = meetup_api_request('groups?sign=true&group_urlname=' + r.group(1))

    results = api_response.get('results')
    if results is None:
        return False

    return results[0].get('id', False)

def meetup_api_request(url):
    base_url = 'https://api.meetup.com/2/'
    api_url = base_url + url + '&key=' + MEETUP_API_KEY

    response = requests.get(api_url)

    return json.loads(response.content)

