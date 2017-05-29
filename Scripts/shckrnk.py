import requests
from bs4 import BeautifulSoup
import datetime

r = requests.get('https://www.hackerrank.com/contests')
soup = BeautifulSoup(r.content,"lxml")

class contest(object):
    start = "";
    name = "";
    end = "";    
    def __init__(self,name,start,end):
        self.name = name
        self.start = start
        self.end = end
t = datetime.datetime.now()
mydivs = soup.findAll("div",{"class": "contest-name"})
attr = soup.findAll(attrs = {"itemprop": "startDate"})
att2 = soup.findAll(attrs = {"itemprop": "endDate"})
l = len(mydivs)
nare = []

for i in range(0,l-1):
    nare.append(contest(mydivs[i+1].text,attr[i]['content'],att2[i]['content']))

for i in range(len(nare)):
    mn = int(nare[i].start[5:7])
    dt = int(nare[i].start[8:10])
    hrs1 = int(nare[i].start[11:13])
    mts1 = int(nare[i].start[14:16])
    hrs2 = int(nare[i].end[11:13])
    mts2 = int(nare[i].end[14:16])
    mts1 = mts1 + 30;
    if(mts1>=60):
	mts1 = mts1-60
	hrs1 = hrs1+6
    else:
	hrs1 = hrs1+5
    if(hrs1>=24):
	hrs1 = hrs1 - 24
    mts2 = mts2 + 30;
    if(mts2>=60):
	mts2 = mts2-60
	hrs2 = hrs2+6
    else:
	hrs2 = hrs2+5
    if(hrs2>=24):
	hrs2 = hrs2 - 24
    if mn >= t.month:
        if mn == t.month:
	    if dt>t.day:
                print(nare[i].name)
        	print("Start Date: " + nare[i].start[0:10])
                print("End Date: " + nare[i].end[0:10])
	        print("Start time: " + str(hrs1) + ":" + str(mts1) + ":" + nare[i].start[17:-5])
                print("End time: " + str(hrs2) + ":" + str(mts2) + ":" + nare[i].end[17:-5])
                print("  ")
		   
	else:
	   print(nare[i].name)
	   print("Start Date: " + nare[i].start[0:10])
           print("End Date: " + nare[i].end[0:10])
	   print("Start time: " + str(hrs1) + ":" + str(mts1) + ":" + nare[i].start[17:-5])
           print("End time: " + str(hrs2) + ":" + str(mts2) + ":" + nare[i].end[17:-5])
	   print("  ")
           
