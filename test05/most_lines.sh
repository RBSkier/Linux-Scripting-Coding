#!/bin/dash

most_line=0
file_most_line="$1"

for file in "$@"
do
    line=$(wc -l < "$file")
    if [ "$line" -gt "$most_line" ]; then
        most_line=$line
        file_most_line="$file"
    fi
done

echo "$file_most_line"

exit 0