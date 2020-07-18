#!/bin/bash
read -p "User, enter a number: " x
orig=$[$x]
res=0
while [ $x -gt 0 ]
do
res=$[$res+x]
x=$[$x-1]
done
echo "$orig --> $res"
