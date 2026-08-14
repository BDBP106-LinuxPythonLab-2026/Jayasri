#!/bin/bash

echo "Enter the filename:"
read file 

if [ -e "$file" ];then

	if [ -x "$file" ];then 
		echo "The file exists and it is executable."
	else 
		echo "The file exists but it is not executable."
	fi

else 
	echo "The files does not exist."
fi

