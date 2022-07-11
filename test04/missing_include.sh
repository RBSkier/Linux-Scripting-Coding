#!/bin/dash

for file in "$@"
do
    for include_file in $(grep -o "#include \"[a-z]*.h\"" "$file" | sed -E "s/#include \"([a-z]*.h)\"/\1/g")
    do
        if ! [ -e "$include_file" ]
        then
            echo "$include_file included into $file does not exist"
        fi
    done
done