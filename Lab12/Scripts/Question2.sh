#!/bin/bash

n=50
for (( i=0; i<=$n; i++ ))
do 
	if [ $((i % 2)) == 0 ]; then
		echo "$i"
	fi
done



