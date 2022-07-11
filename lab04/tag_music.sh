#!/bin/dash

for dir in "$@"
do
	album=$(basename "$dir")
	year="$(echo "$album" | sed -E 's/.* //g')"

	for mp3file in "$dir"/*.mp3
	do
		title=$(basename "$mp3file" .mp3| sed -E 's/^[0-9]* - (.*) - .*$/\1/g')
		artist=$(basename "$mp3file" .mp3 | sed -E 's/.* - //g')
		track=$(basename "$mp3file" .mp3| sed -E 's/ .*//g')		
		id3 -t "$title" -a "$artist" -A "$album" -y "$year" -T "$track" "$mp3file" >/dev/null
	done
done

exit 0
