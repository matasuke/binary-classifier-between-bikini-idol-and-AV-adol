import argparse

#The number of images bing search API allows you to download per one request:
LIMIT = 150

def get_arguments():

    languages = ['es-AR','en-AU','de-AT','nl-BE','fr-BE','pt-BR','en-CA','fr-CA','es-CL','da-DK','fi-FI','fr-FR','de-DE','zh-HK','en-IN','en-ID','en-IE','it-IT','ja-JP','ko-KR','en-MY','es-MX','nl-NL','en-NZ','no-NO','zh-CN','pl-PL','pt-PT','en-PH','ru-RU','ar-SA','en-ZA','es-ES','sv-SE','fr-CH','de-CH','zh-TW','tr-TR','en-GB','en-US','es-US']

    mode = ['Off', 'Moderate', 'Strict']

    parser = argparse.ArgumentParser(description = 'This script collects image urls via Bing search API')
    parser.add_argument(
            'search_word', type=str,
            help="input word you want to search on bing images search")
    parser.add_argument(
            '-c','--count', type=int, default=150,
            help="The number of image urls you want par request")
    parser.add_argument(
            '-o','--offset', type=int, default=0,
            help="The number of image urls you want to skip")
    parser.add_argument(
            '--mkt', type=str, default="ja-JP", choices = languages,
            help="The market where the results come from") 
    parser.add_argument(
            '-s', '--safeSearch', type=str, default="Off", choices = mode,
            help="A filter used to filter results for adult content")
    parser.add_argument(
            '-f', '--saveFile', type=str, default="download_list.csv",
            help="file name for saving list of image urls")
    parser.add_argument(
            '-i', '--iterate', type=int, default=1,
            help="The number of iteration you want to sent requests")

    args = parser.parse_args()


    if args.count > LIMIT:
        raise Exception('The number of count must be less than {0}'.format(LIMIT))


    return args
