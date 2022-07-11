#!/bin/dash
for file in *.jpg
do
	fileNew=$(echo "$file"|sed -E 's/^(.*)\.jpg$/\1.png/g')
	if [ -e "$fileNew" ]
	then
		echo "$fileNew already exists" >&2
		exit 1
	else
		gm convert "$file" "$fileNew" 2> /dev/null && rm "$file"
	fi
done

exit 0
