#!/bin/dash

for htm_file in *.htm
do
    html_file=$(echo "$htm_file" | sed 's/\.htm/\.html/g')
    if [ -e "$html_file" ]
    then
        echo "$html_file exists" >&2
        exit 1
    else
        mv "$htm_file" "$html_file"
    fi
done

exit 0