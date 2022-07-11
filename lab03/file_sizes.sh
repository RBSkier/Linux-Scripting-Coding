#!/bin/bash
for file in *
do
	if [ -f "$file" ]
	then
		line=$(cat "$file" |wc -l) 
		if [ $line -lt 10 ]
		then
			smallFiles="$smallFiles $file"
		elif [ $line -ge 10 ] && [ $line -lt 100 ]
		then
			mediumFiles="$mediumFiles $file"
		else
			largeFiles="$largeFiles $file"
		fi
	fi
done

echo "Small files:$smallFiles"
echo "Medium-sized files:$mediumFiles"
echo "Large files:$largeFiles"

exit 0
