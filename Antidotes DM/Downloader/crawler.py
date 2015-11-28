import urllib2
import re
import requests
from copy import copy
try:
    flag=1
    target = open('Proxy.txt', 'r')
    target_lst = target.read()
    target_lst = target_lst.split()
    address = target_lst[0]
    port = target_lst[1]
    user = target_lst[2]
    password = target_lst[3]

    http_proxy  = "http://" + user + ":" + password + "@" + address + ":" + port
    https_proxy = "http://" + user + ":" + password + "@" + address + ":" + port
    ftp_proxy   = "http://" + user + ":" + password + "@" + address + ":" + port

    proxydict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

except:
    flag=0

FileTypes={'.png':1,'.jpeg':1,'.jpg':1,'.mp3':1,'.mp4':1,'.mkv':1,'.flv':1,'.pdf':1,'.zip',:1,'.txt':1,'.doc':1,'.ppt':1,'.rar':1,'.gif':1,'.gz':1}

class Web_crawler(object):
    
    def __init__(self,url):
        self.url=url
        self.Crawl()
        
    def Crawl(self):
        if flag==1:
            proxy = urllib2.ProxyHandler(proxydict)
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
    
        r = re.compile('<a href[\s]*="[\w,\s,\d,:]*">')
        links = r.findall(urllib.urlopen(self.url).read())
        self.links = copy(links)
        for i in xrange(0,len(links),5):
                self.download5(i)

    def download5(self,index):
        try:
            for j in xrange(0,5):
                link=self.links[index+j]
                for typs in FileType:
                    if typs in link:
                        thread.start_new_thread(self.downloader,(link,typs))
        except:
                for j in xrange(0,len(self.links)%5):
                link=self.links[index+j]
                for typs in FileType:
                    if typs in link:
                        thread.start_new_thread(self.downloader,(link,typs))

    def downloader(self,link,typs):
        x=link.find('="')
        y=link.find(typs)
        filename=links[y-6:y]+typs
        link=link[x:-2]
        try:
            if flag==1:
                r=request.get(link,stream=True,proxies=proxydict)
            else :
                r=request.get(link,stream=True)
            with open(filename,'wb')
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
        except:
            return

        
                    
                    
        
