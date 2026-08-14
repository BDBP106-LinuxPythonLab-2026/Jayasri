#!/bin/bash

echo "Enter the filename:"
read file 

if [ -e "$file" ]; then
	echo "The file exists."
	exit 200

else 
	echo "The files does not exist."
	exit 201
fi

