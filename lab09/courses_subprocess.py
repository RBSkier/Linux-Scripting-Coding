#!/usr/bin/env python3

import re, sys, subprocess

argv1 = sys.argv[1]
web = "http://timetable.unsw.edu.au/2022/" + argv1 + "KENS.html"
cmd = "curl --location --silent " + web
content = subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,encoding="utf8")
pattern="""<td class="data"><a href="({}[0-9]+).html">([^<]+)</a></td>""".format(argv1)
matches = re.findall(pattern, str(content))

courses = []
for match in matches:
  if match[0] != match[1]:
    course = match[0] + " " + match[1]
    if course not in courses:
      courses.append(course)
courses.sort()
for course in courses:
  print(course)
