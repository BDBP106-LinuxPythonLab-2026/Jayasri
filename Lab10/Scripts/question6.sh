#!/bin/bash

echo 'Input a number: '
read n

if [ "$n" -gt 100 ]; then 
	echo 'The number is greater than 100.'
else 
	echo 'The number is not greater than 100.'
fi

