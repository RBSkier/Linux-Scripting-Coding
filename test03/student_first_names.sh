#!/bin/dash
cut -d '|' -f 2,3 |sort|uniq|cut -d '|' -f 2|sed -E 's/^.*, ([a-zA-Z]+) .*$/\1/g'|sort
