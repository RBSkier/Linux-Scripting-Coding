#!/bin/dash

if [ $# -eq 2 ]; then
    number=$1
    name=$2
    count=1

    while [ "$count" -le "$number" ]
    do
        echo "hello $name" > "hello$count.txt"
        count=$((count + 1))
    done
fi

exit 0