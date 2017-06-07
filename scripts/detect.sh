#!/bin/sh

if [ ! -e $1 && ! -e $2]; then
    echo "USAGE: bash $CMDNAE [source dir] [target dir]" 1>$2
    exit 1
fi


SOURCE_PATH=$1
TARGET_PATH=$2

for DIRPATH in ${SOURCE_PATH}*
do
    python detect.py ${DIRPATH} ${TARGET_PATH}
done

