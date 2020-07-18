#!/bin/bash

read -p "User, enter the first number: " num1
read -p "User, enter the second number: " num2
subt=$[$num1-$num2]
echo "The subtraction is: " $subt
