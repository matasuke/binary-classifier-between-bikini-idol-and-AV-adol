from bs4 import BeautifulSoup
import requests
import os


URL_BASE = "http://juneaidoru.web.fc2.com/"

dataset_dir = os.getcwd()

#save_dir_name
dirname = "ADimages"
save_file_path = dataset_dir + "/" + dirname


def download_images():
    KEYWORD = range(1990, 1997)
    print("Downloading images ....")

    if not os.path.exists(save_file_path):
        os.mkdir(save_file_path)
    os.chdir(save_file_path)

    for keyword in KEYWORD:
        print("Start downloading " + str(keyword) + "'s")
        _download(keyword)


def _download(keyword):
    
    IMAGES = []
    
    r = requests.get(URL_BASE + str(keyword) + ".html")
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'lxml')
        imgs = soup.find_all('img')
        for img in imgs:
            if URL_BASE in img['src']:
                IMAGES.append(img['src'][36:-4])
   
    for img in IMAGES:
        pwd = os.getcwd()
        file_path = pwd + "/" + img + ".jpg"
        
        r = requests.get(URL_BASE + "gazou/" + img + ".jpg")
        if r.status_code == 200:
            print(file_path)
            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size = 1024):
                    f.write(chunk)


if __name__ == "__main__":
    download_images()

