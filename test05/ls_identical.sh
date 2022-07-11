#!/bin/dash

for dir1_file in $1/*
do
    if [ -e "$dir1_file" ]; then
        dir1_file_basename=$(basename "$dir1_file")
        dir2_file=$(find $2 -name "$dir1_file_basename")
        if [ -e "$dir2_file" ]; then
            if diff "$dir1_file" "$dir2_file" >/dev/null; then
            echo "$dir1_file_basename"
            fi
        fi
    fi
done

exit 0