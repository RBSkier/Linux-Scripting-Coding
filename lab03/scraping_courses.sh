#!/bin/bash
if [ $# -ne 2 ]
then
	echo "Usage: $0 <year> <course-prefix>" >&2
	exit 1
fi
#
if [ $1 -ge 2019 ] 2>/dev/null && [ $1 -le 2022 ] 2>/dev/null
then
	year=$1
	code=$2

	(curl -sL "https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:$year%20+unsw_psubject.studyLevel:undergraduate%20+unsw_psubject.educationalArea:$code*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:ugrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0";curl -sL "https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:$year%20+unsw_psubject.studyLevel:postgraduate%20+unsw_psubject.educationalArea:$code*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:pgrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0") |
	jq -r '.contentlets | .[] | (.code + " " + .title)'| 
	tr -s " " |
	sort | 
	uniq

else
	echo "$0: argument 1 must be an integer between 2019 and 2022" >&2
	exit 1
fi

exit 0
