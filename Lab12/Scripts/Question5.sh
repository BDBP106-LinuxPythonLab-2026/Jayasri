#!/bin/bash

function divide {
	local var1=$1
	local var2=$2
	if [ $var2 -eq 0 ]; then
		echo "Undefined"
		return
	fi
	local q=$(echo "scale=2 ; $var1 / $var2" | bc)
	local r=$(echo "scale=2 ; $var1 % $var2" | bc)
	echo "Quotient is: $q"
	echo "Remainder is: $r"
}

divide 44 2

