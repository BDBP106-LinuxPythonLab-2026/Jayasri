#!/bin/bash

a=$1
b=$2
c=$3
d=$4
e=$5
if [ $# -eq 4 ]; then 
	echo "$a $b $c $d"
else 
	echo "The number of arguments is not 4"
	exit 300
fi

