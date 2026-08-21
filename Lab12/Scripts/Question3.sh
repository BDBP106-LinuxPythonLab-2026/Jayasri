#!/bin/bash

echo -n "Input number: "
read n

i=1
until [ $i -gt 15 ]
do
	echo "$i * $n = $((i * n))"
	i=$((i + 1))
done

