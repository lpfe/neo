#!/bin/bash


if [ $# -eq 0 ]; then
    echo "Enter the country name~!!"

else
    case "$1" in
        ko) echo "Soeul";;
        us) echo "Washinton";;
        cn) echo "Beijing";;
        jp) echo "Tokyo";;
        *) echo "Your entry => $1 is not in the list.";;
    esac
fi