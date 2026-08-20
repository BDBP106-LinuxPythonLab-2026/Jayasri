#!/bin/bash

echo -n "Input the file/directory name: "
read file

# '-e' checks if the file exists or not
if [ -e "$file" ]; then
	echo "The file exists."
fi

# '-s' checks if the file is non-empty or not
if [ -s "$file" ]; then
	echo "The file is non-empty."
fi

# '-f' checks if the given input is a file or not
if [ -f "$file" ]; then
	echo "The given input is a file."
fi

