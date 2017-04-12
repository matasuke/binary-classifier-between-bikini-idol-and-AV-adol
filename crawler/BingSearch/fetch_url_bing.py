import http.client
import requests
import base64
import json
import os
import csv
import time

import settings
import cmd_options

#bing search api url
BASE_URL = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search'

#set api key
API_KEY = settings.BING_SEARCH_API_KEY

#wait time to sent next request
TIME_OUT = 1


class downloadImgs():
    
    def __init__(self, querry, count=50, offset=0, mkt='ja-JP', safeSearch='Off', iteration = 1):
        self.headers = {
            'Ocp-Apim-Subscription-Key': API_KEY
            }
        self.params = {
                'q': querry,
                'count': count,
                'offset': offset,
                'mkt': mkt,
                'safeSearch': safeSearch,
                }
        self.querry = querry
        self.count = count
        self.offset = offset
        self.mkt = mkt,
        self.safeSearch = safeSearch
        self.iteration = iteration
        self.list = []

    def _createList(self):
        r = requests.get(BASE_URL, params=self.params, headers=self.headers).json()
        for i in range(0, len(r['value'])):
            url = r['value'][i]['contentUrl']
            print(url)
            self.list.append([url])
        
    def createLists(self, saveFile="download_list.csv"):
        for i in range(0, self.iteration):
            self.list = []
            self._createList()
            self.params['offset'] += self.count
            if i == 0:
                self.saveList(saveFile, head=True)
            else:
                self.saveList(saveFile, head=False)

            time.sleep(TIME_OUT)

    def saveList(self, saveFile='csvfiles/download_list.csv', head=True):
        
        if head == True:
            header = [
                    ['querry', self.querry],
                    ['count', self.count],
                    ['offset', self.offset],
                    ['mkt', self.mkt],
                    ['safeSearch', self.safeSearch],
                    ['iteration', self.iteration],
                    ['Num of Urls', self.count * self.iteration],
                    ['Next offset', self.offset + self.count * self.iteration]
                    ]

        with open(saveFile, 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            if head == True:
                writer.writerows(header)
            writer.writerows(self.list)


if __name__ == '__main__':
    args = cmd_options.get_arguments()
    querry = args.search_word
    count = args.count
    offset = args.offset
    mkt = args.mkt
    safeSearch = args.safeSearch
    saveFile = args.saveFile
    iterate = args.iterate

    bing = downloadImgs(querry, count, offset, mkt, safeSearch, iterate)
    bing.createLists(saveFile)
