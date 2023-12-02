#!/bin/sh

cookie="$(<cookie.txt)"

if [ -z $1 ]
then
	echo "Input day missing!"
else
	day=`printf %02d $1`
	cp -nv "main/day00.py" "main/day$day.py"
	curl --cookie "session=$cookie" "https://adventofcode.com/2023/day/$1/input" > "input/day$day.txt"
fi
