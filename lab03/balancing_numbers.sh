#!/bin/bash
cat $1|tr "01234" "<" | tr "6789" ">"

exit 0
