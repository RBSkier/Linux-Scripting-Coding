#!/bin/dash

file="$1"
backup_num=0

while [ -e ".$file.$backup_num" ]
do
    backup_num=$(($backup_num + 1))
done

cat "$file" > ".$file.$backup_num" && echo "Backup of '$file' saved as '.$file.$backup_num'"


exit 0