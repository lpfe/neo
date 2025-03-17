#!/bin/bash

str="Hello, world, Linux!"
echo "${str:0:5}"               # str 0에서 5번째까지 출력
echo "${str:7}"                 # 이후부터 출력
echo "${str:-7}"                # 뒤에서 7까지 출력
