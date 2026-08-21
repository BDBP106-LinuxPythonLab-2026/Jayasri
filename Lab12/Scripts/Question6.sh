#!/bin/bash

function maximum {
	value1=$1
	value2=$2
	if [ $value1 -gt $value2 ]; then
		echo "$value1 is greater."
	else 
		echo "$value2 is greater."
	fi
}
maximum 20 10

