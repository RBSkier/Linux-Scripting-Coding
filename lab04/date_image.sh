#!/bin/dash

for image in $@
do
	date=$(ls -l "$image"	| cut -d ' ' -f 6-8)
	convert  -gravity south -pointsize 36 -draw "text 0,10 '$date'" "$image" "temporary_$image"
done

exit 0