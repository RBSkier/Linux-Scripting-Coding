#!/bin/dash

backup_num=0

while [ -e ".snapshot.$backup_num" ]
do
    backup_num=$((backup_num + 1))
done

mkdir ".snapshot.$backup_num" && echo "Creating snapshot $backup_num"

for file in *
do
    if [ "$file" != "snapshot-save.sh" ] && [ "$file" != "snapshot-load.sh" ]
    then
        cp -r "$file" ".snapshot.$backup_num/"
    fi
done

exit 0