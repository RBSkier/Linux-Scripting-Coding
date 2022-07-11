#!/bin/bash
##if the number of arguments is not 2, print the error message
if [ $# -ne 2 ]
then
	echo "Usage: ./echon.sh <number of lines> <string>" >&2
	exit 1
fi
##if the first argument isn't a non-negative integer, print the error message
if grep '[^0-9]' <<< $1 >/dev/null
then	
	echo "./echon.sh: argument 1 must be a non-negative integer" >&2
	exit 1
fi
#
times=$1
string=$2
#print the string n times
while [ $times -gt 0 ]
do
	echo $string
	times=$(($times-1))
done

exit 0
