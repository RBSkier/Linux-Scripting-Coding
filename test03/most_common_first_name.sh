#!/bin/dash
grep -E 'COMP(2041|9044)'|cut -d '|' -f 3|sed -E 's/^.*, ([A-Z][a-z]*) .*$/\1/g'|sort|uniq -c|sort -nr|head -1|sed -E 's/^.*[[:digit:]] ([A-Z][a-z]*).*$/\1/g'
