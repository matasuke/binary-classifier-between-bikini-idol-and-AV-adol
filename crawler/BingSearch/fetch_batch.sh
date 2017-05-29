#!/bin/sh

if [ ! -e $1 ]; then
    echo "USAGE: bash $CMDNAE [file.csv]" 1>$2
    exit 1
fi

for line in `cut -d ',' -f 2 $1`
do
    python fetch_url_bing.py $line -i 5
done
    
