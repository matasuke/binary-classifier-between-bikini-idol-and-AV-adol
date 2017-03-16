#This scripts download the images of AV actoresses

from bs4 import BeautifulSoup
import requests
import os

URL_BASE = "http://actress.dmm.co.jp/-/list"

#img download path
IMG_URL = "http://pics.dmm.co.jp/mono/actjpgs/thumbnail/"

dataset_dir = os.getcwd()

#save_dir_name
dirname = "AVimages"
save_file_path = dataset_dir + "/" + dirname


def download_images():
    KEYWORDS = _get_urls()
    print("Downloading images ....")

    if not os.path.exists(save_file_path):
        os.mkdir(save_file_path)
    os.chdir(save_file_path)

    for keyword in KEYWORDS:
            _download(keyword)


def _download(keyword):

    IMAGES = []
    last_path = "/=/keyword=" + keyword + "/" 
    r = requests.get(URL_BASE + last_path)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")
        imgs = soup.find_all('img')
        for img in imgs:
            if IMG_URL in img['src']:
                IMAGES.append(img['src'][45:-4])

    for img in IMAGES:
        pwd = os.getcwd()
        file_path = pwd + "/" + img + ".jpg"
        r = requests.get(IMG_URL + img + ".jpg")
        if r.status_code == 200:
            print(file_path)
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size = 1024):
                    f.write(chunk)


def _get_urls():

    BASE_KEYWORD = "/-/list/=/keyword="
    KEYWORD = []
    
    r =requests.get(URL_BASE) 
    soup = BeautifulSoup(r.content, "lxml")
    links = soup.find_all('a')
   
    for link in links:
        if BASE_KEYWORD in link['href']:
            KEYWORD.append(link['href'][18:-1])

    return KEYWORD
 
#def _get_num_of_pages():


if __name__ == "__main__":
    download_images()
