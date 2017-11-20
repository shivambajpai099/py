import requests
from bs4 import BeautifulSoup
import datetime

r = requests.get('http://www.codechef.com/contests')
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
mydivs = soup.findAll("td")
print(mydivs)

l = len(mydivs)
nare = []

for i in range(15,40,4):
    yr = int(mydivs[i].text[7:11])
    mn = mydivs[i].text[3:6]
    dt = int(mydivs[i+1].text[0:2])
    
    if yr==2017 and mn == "Jun" and dt>t.day:
        nare.append(contest(mydivs[i-1].text,mydivs[i].text,mydivs[i+1].text))
	
print(len(nare))

for i in range(len(nare)):
	print(nare[i].name)
        print("Start Date: " + nare[i].start[0:11])
        print("End Date: " + nare[i].end[0:11])
	print("Start time: " +nare[i].start[13:])
        print("End time: " + nare[i].end[13:])
        print("  ")
