import requests
import time
import csv
import os
import argparse

def download_images(source, target="../../bing_images", ignore=0):
    
    if not os.path.isfile(source):
        print("source directory doesn't exist")
        sys.exit(1)
        
    if not os.path.isdir(target):
        os.mkdir(target)
    
    with open(source, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if row[0][:10] == 'http://www':
                if i - 8 < ignore:
                    pass
                else:
                    print('downloading.... ', row[0])
                    time.sleep(1)
                    r = requests.get(row[0])
                    file_name = target + '/' + str(i) + '.jpg'
                    with open(file_name, 'wb') as f:
                        for chunk in r.iter_content(chunk_size = 1024):
                            f.write(chunk)
                        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'this script downloads images based on given csv file')
    parser.add_argument(
            'source_file', type=str,
            help="choose csv file"
            )
    parser.add_argument('-t', '--target_dir', type=str, default='../../bing_images',
            help="choose target directory"
            )
    parser.add_argument('-i', '--ignore', type=int, default=0,
            help="The number of ignored rows")
    
    args = parser.parse_args()

    download_images(args.source_file, args.target_dir, args.ignore)
