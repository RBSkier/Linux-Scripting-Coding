#!/bin/dash
cut -d '|' -f 2 |sort|uniq -c|tr -s ' '|grep ' 2 '|cut -d ' ' -f 3|sort -n
