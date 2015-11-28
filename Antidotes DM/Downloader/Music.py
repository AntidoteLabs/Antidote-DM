import urllib2
import re
import requests

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

class music(object):

    def __init__(self, queary):
        self.queary = queary
        url = self.urlCreator(self.queary)
        self.song_url = self.search(url)

    def search(self, url):
        print url
        r = requests.get(url, stream=True, proxies=proxyDict)
        with open('test.txt', 'w') as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
##        proxy = urllib2.ProxyHandler(proxyDict)
##        opener = urllib2.build_opener(proxy)
##        urllib2.install_opener(opener)
##        web_page=urllib2.urlopen(url)
##        web_page=web_page.read()
        tar = open('test.txt', 'r')
        target = tar.read()
        start_index = target.find('a> <a href="http://') + 20 #Do not remove the space in between <a> tags
        end_index = target.find('.mp3"', start_index)
        return target[start_index:end_index+1]

    def urlCreator(self, queary):
        queary = re.sub(' ', '_',queary)
        url = 'http://emp3world.to/search/' + queary + '_mp3_download.html'
        return url

