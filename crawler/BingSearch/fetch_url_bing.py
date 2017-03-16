import http.client
from urilib import request, parse, error
import base64
import json
import os

import settings
import cmd_options

#the number of images Bing search API allow you to download per one request:
LIMIT = 150

#bing search api url
BASE_URL = 'https://api.cognitive.microsoft.com'

#set api key
API_KEY = settings.BING_SEARCH_API_KEY

#wait time to sent next request
TIME_OUT = 5

params = {
        'q': 
        }


class downloadImgs():
    
    def __init__(self, querry, count, offset, mkt, safeSearch, saveFile):
        self.headers = {
            'Opt-Apim-Subscription-Key': API_KEY
            }
        self.params = urilib.parse.urlencode({
                'q': querry,
                'count': count,
                'offset': offset,
                'mkt': mkt,
                'safeSearch': safeSearch,
                })

    def createList(self):
        try:
            conn = http.client.HTTPConnection(BASE_URL)
            conn.request('GET', '/bing/v5.0/images/search?%s' % self.params,)
def main()

if __name__ == '__main__':
    args = cmd_options.get_arguments()
