#!/usr/local/bin/python3.6

#ptt spider


import urllib.request
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://www.ptt.cc/bbs/Soft_Job/M.1500388186.A.5CB.html", headers=headers)
response = urllib.request.urlopen(req).read()

soup =  BeautifulSoup(response,"html.parser")
main_content = soup.find(id="main-content")
infomation = main_content.select('div.article-metaline')

#print(main_content)

#print(infomation)

#for a in infomation:
#    print(a)



date = infomation[2].select('span.article-meta-value')[0].string
write = infomation[0].select('span.article-meta-value')[0].string
tite = infomation[1].select('span.article-meta-value')[0].string
print("日期：%s,作者：%s,標題：%s"%(date,write,tite))




    #print("日期：%s,作者：%s,標題：%s")
    #print("內文：%s")
    #print("看板名稱：%s")

