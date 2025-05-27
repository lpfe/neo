#!/bin/bash

set -- $(getopt -q u:g:c:d:s:k:m "$@")        # user 옵션만 받는다

echo
while [ -n "$1" ]                # == while [ $# -n 0 ]  == 전체 파라미터 카운트가 0이 아니면 == $1이 있으면(파라미터가 있으면~)
do
    case "$1" in
        -u) param="$2"
            echo "-u (uid) option, with parameter value $param"
            shift;;
        -g) param="$2"
            echo "-g (gid) option, with parameter value $param"
            shift;;
        -c) param="$2"
            echo "-c (comment) option, with parameter value $param"
            shift;;
        -d) param="$2"
            echo "-d (home directory) option, with parameter value $param"
            shift;;
        -s) param="$2"
            echo "-s (shell) option, with parameter value $param"
            shift;;
        -k) param="$2"
            echo "-k (initial scripts directory) option, with parameter value $param"
            shift;;
        -m) echo "-m (make home directory) option"
            shift;;
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
