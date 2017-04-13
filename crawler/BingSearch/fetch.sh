#!/bin/bash

if [ -f $1 ]; then
    awk -F, '{$2}'
