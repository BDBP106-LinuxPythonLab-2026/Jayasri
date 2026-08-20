#!/bin/bash

echo -n "Give the name of the string: "
read string

# '-z' checks if the string is empty 
if [ -z "$string" ]; then
	echo "The string is empty."
else 
	echo "The string is not empty."
fi

# '-n' checks if the string is non empty
if [ -n "$string" ]; then
	echo "The string is non-empty."
else
	echo "The string is empty."
fi

