#coding: utf-8

import re 
import requests  
from pyquery import PyQuery as pq

def getHtmlContext(url, code="utf-8"):  
    try:  
        r =requests.get(url)  
        r.raise_for_status()  
        r.encoding = code  
        return r.text  
    except:  
        return ""   
    
    
def main():  
    print("start")
    baiduUrlWithName='http://www.baidu.com/s?wd=lupc7'  
    doc= pq(getHtmlContext(baiduUrlWithName))
    mlist = doc('#content_left h3.t a').items()
    i=0
    for li in mlist :
        i=i+1
        print('title:'+li.text())
        print('url:'+li.attr('href'))
    print(i)
    print("end")  
  
  
main()
