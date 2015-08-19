#coding=utf-8

import threading
import urllib2,re,smtplib  

def getHot(newslink):
    response = urllib2.urlopen(newslink)
    html = response.read()
    hotHtml=re.split('<div class="tags dot_x_t">|<div class="share">',html)
    hotList=re.split('return false">|</a>',hotHtml[1])
    return (hotList[1::2])
    
def getNewsList(data):
    response = urllib2.urlopen('http://cctv.cntv.cn/lm/xinwenlianbo/'+data+'.shtml')
    html = response.read()
    newshtml = re.split('<div class="md_bd">|<script>',html)
    newsListTemp = re.split('<li><a href="|" target="',newshtml[2])
    newsList=newsListTemp[1::2]
    print data + "热词"
    for i in range(1,len(newsList)):
    	hotList=getHot(newsList[i])
    	for j in range(0,len(hotList)):
     		print hotList[j],

    print ""
    
    

if __name__=="__main__":
    
    data0=20150801

    for i in range(0,7):
    	getNewsList(str(data0+i))

