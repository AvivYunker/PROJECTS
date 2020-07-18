#!/bin/bash
read -p "User, enter the lower edge: " lower
read -p "User, enter the upper edge: " upper

while [ $lower -le $upper ]
do
echo $lower
lower=$(($lower+1))
done
echo -e "\nDONE\n"
