from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import os


BASE_URL = 'https://xcity.jp/idol/'

#choose save dir
current_dir = os.getcwd()
save_dir = 'AVimages'
save_dir_path = current_dir + "/" + save_dir


def download_all_images():
   
    if not os.path.isdir(save_dir_path):
        os.mkdir(save_dir_path)
    
    urls = []
    names = []

    # create a list of all of AV actresses which are registered on Xcity
    names, urls = create_all_of_list()
    for name, url in zip(names, urls):
        print("Downloading", "http://", url)
        r = requests.get('https:' + url)
        file_path = save_dir_path + '/' + name + '.jpeg'
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024):
                f.write(chunk)

    
    
def create_all_of_list():
    
    names = []
    urls = []

    Hiragana = ['あ', 'か', 'さ', 'た', 'な', 'は', 'ま', 'や', 'ら', 'わ']
    
    for H in Hiragana:
        tmp_names, tmp_urls = create_part_of_list(H)
        names += tmp_names
        urls += tmp_urls

    return names, urls
        

# create list of name and image url of AV actress, but partial one. it means it just creates list of AV actress assigned to one 5 characters(for example, A,I,U,E,O)
def create_part_of_list(hiragana):

    names = [] # save names
    urls = [] # save url

    last_page = _get_last_page(hiragana)

    for i in tqdm(range(1, int(last_page)+1)):
        
        print("Creating a list of col ", hiragana, " ",  "page ", i)

        BASE_QUERY = '?kana=' + hiragana + '&num=90&page=' + str(i)# page number has to be added at the end
        r = requests.get(BASE_URL + BASE_QUERY)
        soup = BeautifulSoup(r.content, 'lxml')

        #get the name and url of every kind of av actress in one page:
        for itembox in soup.find_all("div", class_="itemBox"):
            for url in itembox.find_all("img"):
                names.append(url['alt'])
                urls.append(url['src'])

    return (names, urls)


def _get_last_page(hiragana):
    BASE_QUERY = '?kana=' + hiragana + '&num=90&page=1'
    
    # get html files 
    r = requests.get(BASE_URL + BASE_QUERY)
    soup = BeautifulSoup(r.content, 'lxml')
    
    #get the number of last page
    pages = soup.find("ul", class_="pageScrl")
    if len(pages.find_all("a")) >= 2:
        page = pages.find_all("a")[-2].contents
    else:
        page = [1]

    return page[0]


if __name__ == "__main__":
    download_all_images()

