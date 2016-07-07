import urllib2
import json

locu_api = '03e568b4b52ee04786467c6ec017b79e9e488888'

def locu_search(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality
    obj = urllib2.urlopen(final_url)
    data = json.load(obj)
    for item in data['objects']:
        print item['name'], item['phone']
