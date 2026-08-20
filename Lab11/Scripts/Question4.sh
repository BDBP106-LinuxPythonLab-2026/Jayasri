#!/bin/bash

val1=Jayashree
val2=Nagesh

if [ $val1 \> $val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi

# > redirects the output to a file. 
# \ tells the shell to treat the next character as it is, rather than as a special operator. 
# hence > does not redirect the output. Instead, > is passed as an argument. 
