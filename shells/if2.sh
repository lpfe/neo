#!/bin/bash

echo "File Name : $0"
echo "Parameter Count : $#"
echo "All Parameter : $@"

# if [ "$#" == 1 ]; then
#     echo Input Two Parameters

elif [ "$1" = "$2" ]; then
    echo Same~!!
else
    echo Not Same~!!
fi