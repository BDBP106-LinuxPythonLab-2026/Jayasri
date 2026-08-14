#!/bin/bash 

echo -n "Give the input-score: "
read score

if [ "$score" -ge 90 ]; then
	echo 'Grade A'
elif [ "$score" -ge 80 ] && [ "$score" -le 89 ]; then
	echo 'Grade B'
elif [ "$score" -ge 70 ] && [ "$score" -le 79 ]; then
	echo 'Grade C'
else
	echo 'FAIL'
fi
