#!/bin/dash
for image in $@
do
	gm display "$image"
	read -p "Address to e-mail this image to?" address
	read -p "Message to accompany image?" message
	echo "$address $message"
	echo "$message"| mutt -s "Images" -e "set copy=no"  -a "$image" -- $address
done
