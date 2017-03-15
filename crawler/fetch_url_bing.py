import argparse
import urllib
import requests
import json
import os
import key

#the number of images Bing search API allows you to download per one request:
LIMIT = 150

#bing search api url
BASE_URL = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"

#set api key
API_KEY = key.BING_SEARCH_API_KEY

#wait time to sent next request
TIME_OUT = 5

#file name for saving list of image urls:
SAVE_FILE = 'download_list.txt'



parser = argparse.ArgumentParser(description = 'This script collects image urls via Bing search API')
parser.add_argument('search_word', type=str, help="input word you want to search on bing images search")
parser.add_argument('--c','--count', type=int, help="The number of image urls you want par request")

parser.add_argument('--o','--offset', type=int, help="The number of image urls you want to skip")

parser.add_argument('--mkt', type=str, help="The market where the results come from", choices=['es-AR','en-AU','de-AT','nl-BE','fr-BE','pt-BR','en-CA','fr-CA','es-CL','da-DK','fi-FI','fr-FR','de-DE','zh-HK','en-IN','en-ID','en-IE','it-IT','ja-JP','ko-KR','en-MY','es-MX','nl-NL','en-NZ','no-NO','zh-CN','pl-PL','pt-PT','en-PH','ru-RU','ar-SA','en-ZA','es-ES','sv-SE','fr-CH','de-CH','zh-TW','tr-TR','en-GB','en-US','es-US'])

parser.add_argument('-s', '--safeSearch', type=str, help="A filter used to filter results for adult content", choices = ['Off', 'Moderate', 'Strict'])

args = parser.parse_args()

if not args.count:
    args.count = 5

elif args.count > LIMIT:
    raise Exception('The number of count must be less than {0}'.format(LIMIT))











