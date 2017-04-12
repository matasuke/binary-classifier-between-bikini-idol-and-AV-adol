#! /bin/bash

files="./csvfiles/AV/*"
for filepath in $files;
do
    python download_img.py $filepath
done
