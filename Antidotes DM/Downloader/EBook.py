import urllib2
import re
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

class Search_ebook(object):
    def __init__(self, query):
        super(Search_ebook, self).__init__()
        self.query = query
        self.url=self.create_search_url(self.query)
        self.books_urls,self.book_names=self.get_books_info(self.url)
        
    def create_search_url(self,query):
        temp1='http://gen.lib.rus.ec/search.php?req='
        temp2='&open=0&view=simple&phrase=1&column=def'
        search_query=query.split()
        search_query=tuple(search_query)
        search_query='+'.join(search_query)
        url=temp1+search_query+temp2
        return url

    def get_books_info(self,url):    
        if flag==1:
            proxy = urllib2.ProxyHandler(proxydict)
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

        web_page=urllib2.urlopen(url)
        web_page=web_page.read()
        
        book_start_urls=[x.start() for x in re.finditer('/get',web_page)]
        book_end_urls=[]
        for i in book_start_urls:
            book_end_urls.append(web_page.find('title',i))
        books_urls=['http://gen.lib.rus.ec'+web_page[book_start_urls[i]:book_end_urls[i]-2] for i in range(len(book_start_urls))]

        book_start_names=[x.start() for x in re.finditer('book/',web_page)]
        book_end_names=[]   
        for i in book_start_names:
            book_end_names.append(web_page.find('</a>',i))
        book_names=[web_page[book_start_names[i]:book_end_names[i]] for i in range(len(book_start_names))]
        book_start_names=[]
        for i in book_names:
            book_start_names.append(i.find('>'))
        book_names=[book_names[i][book_start_names[i]+1:] for i in range(len(book_start_names))]
        books_names=[]
        for books in book_names:
            if '</font>' in books:
                regex=re.compile('</font>[\w,\s,\d,:,(,)]*<')
                bookName=regex.findall(books)
                for x in bookName:
                    if len(x[7:-1])>2:
                        books_names.append(x[7:-1])
            else:
                books_names.append(books)
        return books_urls,books_names
##s=Search_ebook('linear algebra')
##print 'lol'
##print s.book_names
