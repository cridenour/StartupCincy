import json
import urllib
import requests

def base_url():
    return 'http://api.crunchbase.com/v/1/'

def apiCall(api_url):
    """
    Returns dictionary of the response. If anything went wrong anywhere, dictionary with a key of error is returned.
    """
    url = base_url() + api_url

    response = requests.get(url)

    return json.loads(response.content)


def getPermalink(namespace, name):
    """
    Namespace should be plural
    """
    args = urllib.urlencode({'name': name})
    response = apiCall(namespace + '/permalink?' + args)

    return response['permalink']

def getCompany(name, search=False):
    """
    Search to True if we're inputting full company name
    """
    if search:
        name = getPermalink('companies', name)

    if name is '':
        return {'error': True, 'message': 'Could not find company.'}

    return apiCall('company/' + name + '.js')

# TODO: Integrate rest of the API? People integration, financial institutions.