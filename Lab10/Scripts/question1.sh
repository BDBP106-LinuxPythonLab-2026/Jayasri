#!/bin/bash

echo 'Enter the age:'
read age

if [ "$age" -gt 18 ]; then
	echo 'You are an adult.'
else
	echo 'You are a minor.'
fi
