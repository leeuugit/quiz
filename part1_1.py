#!/usr/local/bin/python3.6

#Counting
from collections import Counter

urls = ["http://www.google.com/a.txt","http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg","http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt","https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg","http://gliacloud.com/haha.png"]


namelist = []
for oneurl in urls:
    name = oneurl.replace("//","/").split("/")[-1]
    namelist.append(name)

counts = Counter(namelist)

TopThree = counts.most_common(3)

for show in TopThree:
    print("%s %s"%(show[0],show[1]))