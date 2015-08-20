#coding=utf-8

import threading
import urllib2,re,smtplib
import datetime
from collections import Counter

def getHot(newslink):
	try:
	    response = urllib2.urlopen(newslink)
	    html = response.read()
	    hotHtml=re.split('<div class="tags dot_x_t">|<div class="share">',html)
	    hotList=re.split('return false">|</a>',hotHtml[1])
	    return (hotList[1::2])
	except:
		print "empty url",
		e=[]
		return e
    
def getNewsList(data):
	hotList=[]
	response = urllib2.urlopen('http://cctv.cntv.cn/lm/xinwenlianbo/'+data+'.shtml')
	html = response.read()
	newshtml = re.split('<div class="md_bd">|<script>',html)
	newsListTemp = re.split('<li><a href="|" target="',newshtml[2])
	newsList=newsListTemp[1::2]
	print data, 
	for i in range(1,len(newsList)):
		hotList=hotList+getHot(newsList[i])
	print "...Done"
	return hotList
    
    

if __name__=="__main__":
    day0=datetime.date(2015,1,1)
    paper=[]

    for i in range(0,181):
    	day=day0 + datetime.timedelta(i)
    	paper=paper+getNewsList(str(day.strftime("%Y%m%d")))

    plist=Counter(paper).most_common(30)

    for i in range(0,len(plist)):
    	print plist[i][0],
    	print " ",
    	print plist[i][1]


