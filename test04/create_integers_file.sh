#!/bin/dash

from_num="$1"
to_num="$2"
file="$3"

print_num=$from_num
while [ $print_num -le $to_num ]
do
    echo "$print_num" >> "$file"
    print_num=$(($print_num + 1))
done

exit 0