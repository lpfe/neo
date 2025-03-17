#!/bin/bash

set -- $(getopt -q ab:cd "$@")

echo
while [ -n "$1" ]                # == while [ $# -n 0 ]  == 전체 파라미터 카운트가 0이 아니면 == $1이 있으면(파라미터가 있으면~)
do
    case "$1" in
        -a) echo "Found the -a option";;
        -b) param="$2"
            echo "Found -b option, with parameter value $param"
            shift;;      ## 아무동작 없이 다음으로 넘겨라
        -c) echo "Found the -c option";;
        --) shift
            break;;
        *) echo "$1 is not an option";;
    esac
    shift
done
count=1
for param in "$@"
do
    echo "Parameter #$count: $param"
    count=$[ $count + 1 ]
done
