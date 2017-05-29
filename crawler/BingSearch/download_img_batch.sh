#!/bin/sh

if [ ! -e $1 ]; then
    echo "USAGE: bash $CMDNAE [dir name]" 1>$2
    exit 1
fi

DIRPATH=$1

for FILEPATH in ${DIRPATH}*
do
    #FILE=`basename ${FILEPATH}`
    python download_img.py ${FILEPATH}
done
