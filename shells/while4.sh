#!/bin/bash

row=$1
if [ $# -eq 0 ]; then     # 파라미터 갯수가 0이면
    echo "This program is have to one parameter~!!"
else
    while [[ 10 -gt $row ]]; do         #
        echo $row
        row=`echo "$row"+1 | bc`        # bc == 계산기
    done
fi