import requests
import time
import csv
import os
import argparse
import sys

def download_images(source, target="../../images/Bing", AV=0, ignore=0):
    
    if not os.path.isfile(source) or os.path.splitext(source)[1] != '.csv':
        print("source directory doesn't exist")
        sys.exit(1)

    if AV == 0:
        target = target + '/AVactresses/' + source.split('/')[-1][:-4]
    else:
        target = target + '/idol/' + source.split('/')[-1][:-4]
        
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    
    with open(source, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if row[0][:10] == 'http://www':
                if i - 8 < ignore:
                    pass
                else:
                    try:
                        print('downloading.... ', row[0])
                        #time.sleep(1)
                        r = requests.get(row[0])
                        file_name = target + '/' + str(i) + '.jpg'
                        with open(file_name, 'wb') as f:
                            for chunk in r.iter_content(chunk_size = 1024):
                                f.write(chunk)
                    except requests.exceptions.ConnectionError:
                        print("can't connect the page...") 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'this script downloads images based on given csv file')
    parser.add_argument(
            'source_file', type=str,
            help="choose csv file"
            )
    parser.add_argument('-t', '--target_dir', type=str, default='../../images/Bing',
            help="choose target directory"
            )
    parser.add_argument('-w', '--witch', type=int, default=0,
            help='input type of images'
            )
    parser.add_argument('-i', '--ignore', type=int, default=0,
            help="The number of ignored rows"
            )
    
    args = parser.parse_args()

    download_images(args.source_file, args.target_dir, args.witch, args.ignore)
