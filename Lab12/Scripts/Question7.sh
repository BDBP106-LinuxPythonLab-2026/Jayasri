#!/bin/bash

function directory {
	echo -n "Give the name of the file/directory: "
	read name
	if [ -d $name ]; then
		echo "The directory exists."
		ls $name
	elif [ -f $name ]; then
		echo "The given input is not a directory."
	else 
		mkdir $name
		echo "The new direcotry is created"
	fi
}

directory
