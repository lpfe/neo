#!/bin/bash

# while문

a=1
while [ $a != "0" ]; do
    echo -n "Input (0:Exit) : "
    read a

    if [ $a -eq 0 ]; then
        break;
    elif [ $a -ge 2 -a $a -le 9 ]; then     # [ $a -ge 2 ] && [ $a -le 9 ] 로도 가능
        for ((k=1;k<10;k++))
        do
            echo "$a * $k = `expr $a \* $k `"
        done
    else
        echo "The number of inputs must be between 2 to 9"
    fi
done
echo Exit