from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import os

BASE_URL = 'http://idol.manzoku100.com/akasatana/'

#choose save dir
current_dir = os.getcwd()
save_dir = 'ADimages'
save_dir_path = current_dir + "/" + save_dir


def download_all_images():

    if not os.path.isdir(save_dir_path):
        os.mkdir(save_dir_path)

    urls = []
    names = []

    names, urls = create_all_of_the_lists()
    for name, url in zip(names, urls):
        print("Downloading ", url)
        r = requests.get(url)
        file_path = save_dir_path + '/' + name + '.jpg'
        
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024):
                f.write(chunk)

def create_all_of_the_lists():
    
    names = []
    urls = []

    Hiragana = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa']

    for H in Hiragana:
        tmp_names, tmp_urls = create_part_of_list(H)
        names += tmp_names
        urls += tmp_urls

    return names, urls


def create_part_of_list(hiragana):

    names = []
    urls = []

    NO_IMAGE = "http://pics.dmm.com/mono/actor/printing.jpg"

    last_page = get_last_page(hiragana)

    for i in tqdm(range(1, int(last_page)+1)):

        print("Creating a list of col ", hiragana, " ", "page ", i)
        BASE_QUERY = hiragana + '/' + str(i)
        r = requests.get(BASE_URL + BASE_QUERY)
        soup = BeautifulSoup(r.content, 'lxml')

        for idol_box in soup.find_all('ul', class_="idol-box-125"):
            for a in idol_box.find_all("a"):
                for url in a.find_all("img"):
                    if url['src'] is not NO_IMAGE:
                        names.append(url['src'][31:-4])
                        urls.append(url['src'])

    return (names, urls)

def get_last_page(hiragana):
    BASE_QUERY = hiragana + '/1'

    #get html files
    r = requests.get(BASE_URL + BASE_QUERY)
    soup = BeautifulSoup(r.content, 'lxml')

    #get the number of last page
    num = soup.find('div', attrs={'style':'text-align:left;font-size:14px'})
    if num.contents[0][-8] is '-':
        num = int(num.contents[0][:-13]) + 1
    else:
        num = 1

    return num

if __name__ == '__main__':
    download_all_images()
