#!/bin/bash

# 복합 for 문

row="one two three"

for mon in $row; do
    for ((i=0;i<9;i++)) do
        echo "$mon $i"
    done
done