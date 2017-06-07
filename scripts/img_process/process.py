import cv2
import numpy
import sys
import os
import argparse
from detect import detect

formats = ['jpg', 'png', 'jpeg']

def processImg(source, target):
    source = os.path.abspath(source) + '/'
    dir_path = os.path.abspath(target) + '/' + source.split('.')[-1] + '/'
    files = os.listdir(source)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    os.chdir(dir_path)
    
    for f in files:
        if f.split('.')[-1] in formats:
            f_name = f.split('.')[0] + '_'
            img = cv2.imread(source + f)
            results = detect(img)
            
            for i, img in enumerate(results):
                cv2.imwrite(f_name + str(i + 1) + '.jpg', img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'source_dir', type=str,)
    parser.add_argument(
            'target_dir', type=str)
    args = parser.parse_args()

    processImg(args.source_dir, args.target_dir)
