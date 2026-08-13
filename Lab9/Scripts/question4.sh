#!/bin/bash

#Gives the name of the script
echo 'The file name is: '$0

Name=$1
Age=$2
echo 'The first argument is: '$1
echo 'The second argument is: '$2 

#Number of arguments passed to this script
echo 'The number of arguments passed to this script: '$#

#Represents all the arguments passed to the script
echo 'The array/list of arguments passed to this script: '$@

#The arguments can be stored in an array by enclosing $@ in a ()
listofarg=($@)
echo ${listofarg[0]}


