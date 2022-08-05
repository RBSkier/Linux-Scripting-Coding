#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys

argv1 = sys.argv[1]
url = "http://timetable.unsw.edu.au/2022/" + argv1 + "KENS.html"
content = requests.get(url).text
beautySoup = BeautifulSoup(content,'html.parser')

courses = []
for link in beautySoup.find_all('a'):
  tt = link.get('href')
  cname = link.get_text()
  if tt and len(tt) > 7 and tt[8:] == ".html":
    if tt[:8] != cname:
      d = tt[:8] + " " + cname
      if d not in courses:
        courses.append(d)
    
courses.sort()
for course in courses:
  print(course)

