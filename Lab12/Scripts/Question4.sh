#!/bin/bash

read -ra numbers < nums.txt
echo "The array is: "${numbers[*]}
l=${#numbers[@]}
for (( i=0; i<$l; i++ ))
do
	echo "$((numbers[i] * 2))"
done
