#!/bin/sh

SOURCE_PATH=$1
TARGET_PATH=$2

for DIRPATH in ${SOURCE_PATH}*
do
    python process.py ${DIRPATH} ${TARGET_PATH}
done

