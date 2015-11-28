from urlparse import parse_qs
import urllib2
try:
    compat_str = unicode
except:
    compat_str = str

import re

compiled_regex_type = type(re.compile('')) 

try:
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

    proxy = urllib2.ProxyHandler()
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
except:
    flag=0

import json
import argparse
from copy import copy
from interpret_js import JSInterpreter

class youtube_extractor():
    
    def __init__(self,video_url):
        self.video_url=video_url
        self.get_video_info()
    
    def _search_regex(self, pattern, string, name, default=object(), fatal=True, flags=0, group=None):

        if isinstance(pattern, (str, compat_str, compiled_regex_type)):
            mobj = re.search(pattern, string, flags)
        else:
            for p in pattern:
                mobj = re.search(p, string, flags)
                if mobj:
                    break
        if mobj:
            if group is None:
                # return the first matching group
                return next(g for g in mobj.groups() if g is not None)
            else:
                return mobj.group(group)
        elif default is not NO_DEFAULT:
            return default
        elif fatal:
            raise ValueError('Unable to extract %s' % _name)
        else:
            Warning('unable to extract %s' % _name + bug_reports_message())
            return None    
    
    def get_video_info(self):
        
        url='//www.youtube.com/get_video_info?&video_id='
        
        if 'http:' in self.video_url:
            self.video_id=parse_qs(self.video_url)['http://www.youtube.com/watch?v'][0]
            url='http:'+url+self.video_id
        elif 'https:' in self.video_url:
            self.video_id=parse_qs(self.video_url)['https://www.youtube.com/watch?v'][0]
            url='https:'+url+self.video_id
        for el_type in ['','&el=info', '&el=embedded', '&el=detailpage', '&el=vevo']:
            try:
                video_info=parse_qs(urllib2.urlopen(url+el_type+'ps=default&eurl=&gl=US&hl=en').read())
                self.video_file_urls(video_info,'mp4','medium')
            except:
                continue
      
            
    def video_file_urls(self,video_info,types,quality):
    
        raw_info=video_info['url_encoded_fmt_stream_map'][0].split(',')
        parsed_info=[parse_qs(i) for i in raw_info]
        for i in parsed_info:
            if types in i['type'][0]:
                video_url=i['url'][0]
                if 'sig' in i:
                    video_url += '&signature='+i['sig'][0]
                elif 's' in i:
                    signature=self.signatures(i['s'][0])
                    video_url += '&signature='+signature
        if 'ratebypass' not in video_url:
            video_url += '&ratebypass=yes' 
        print video_url
        self.video_file_url = video_url
   
    def signatures(self,encrypted_sig):
        player_url_json = self._search_regex(r'ytplayer\.config.*?"url"\s*:\s*("[^"]+")',urllib2.urlopen('https://www.youtube.com/watch?v=gCYcHz2k5x0').read(), 'age gate player URL')        
        player_url = json.loads(player_url_json)
        print player_url
        if 'swf' == player_url[-3:]:
            player_version = self._search_regex(r'-(.+?)(?:/watch_as3)?\.swf$', player_url,'flash player', fatal=False)
            
        else:
            player_version = self._search_regex(r'html5player-([^/]+?)(?:/html5player(?:-new)?)?\.js',player_url,'html5 player', fatal=False)

        signature = self.decrypt_signature(encrypted_sig,self.video_id, player_url, age_gate=False)    
    
    def decrypt_signature(self, s, video_id, player_url, age_gate=False):
        if player_url is None:
            raise TypeError('Cannot decrypt signature without player_url')

        if '//' == player_url[0:2]:
            player_url = 'https:' + player_url
        try:
            func = self._extract_signature_function(video_id, player_url, s)
            return func(s)
        except:
            raise TypeError('Could not extract video url')
    
    def _extract_signature_function(self, video_id, player_url, example_sig):
        id_m = re.match(r'.*?-(?P<id>[a-zA-Z0-9_-]+)(?:/watch_as3|/html5player(?:-new)?)?\.(?P<ext>[a-z]+)$',player_url)
        if not id_m:
            raise TypeError('Cannot identify player %r' % player_url)
        player_type = id_m.group('ext')
        player_id = id_m.group('id')
        
        if player_type == 'js':
            code = urllib2.urlopen(player_url)
            code = code.read()
            res = self._parse_sig_js(code)
        
        # Create SWF Interpreter for SWF type
            
        return res
        
    def _parse_sig_js(self, jscode):
        funcname = self._search_regex(
            r'\.sig\|\|([a-zA-Z0-9$]+)\(', jscode,
            'Initial JS player signature function name')

        jsi = JSInterpreter(jscode)
        initial_function = jsi.extract_function(funcname)
        return lambda s: initial_function([s])

s=youtube_extractor('https://www.youtube.com/watch?v=gCYcHz2k5x0')

