#!/bin/dash

time=0
word=$1
url="http://timetable.unsw.edu.au/2022/${word}KENS.html"
touch c.txt
pattern="/${word}/!d"
data=$(curl --location --silent $url /| sed ${pattern} | sed 's/<[^>]*>//g')

for line in $data
do
  $(echo $line | grep "${word}" > /dev/null) 
  if [ $? = 0 ]
  then
    if [ ! $time = 0 ]
    then
      echo "" >> c.txt 
    fi 
    echo "$line\c" >> c.txt
    time=$(expr $t + 1)
  else
    echo " $line\c" >> c.txt
  fi
done
cat -n c.txt | sort -uk2 | sort -n | cut -f2- | sort -k1
rm c.txt
