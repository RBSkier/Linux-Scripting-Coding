#!/bin/dash

snapshot-save.sh

for file in *
do
    if [ "$file" != "snapshot-save.sh" ] && [ "$file" != "snapshot-load.sh" ]
    then
            rm -r "$file"
    fi
done

echo "Restoring snapshot $1"

backup_dir=".snapshot.$1"

for file in "$backup_dir"/*
do
    cp -r "$file" .
done

exit 0
