# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/webscraping
# blog: http://thinkdiff.net
# MIT License

# --------------------------
#  Aljazeera.com Scraping
# --------------------------

'''
urllib
BeautifulSoup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Installing Beautiful Soup
mac: pip3 install bs4
win: pip install bs4

'''

from urllib.request import urlopen 
from bs4 import BeautifulSoup

from . import helper

# Global variables
CACHE       = 3 # minutes
url_aj      = 'http://www.aljazeera.com'
raw_html    = 'html/aj.html'
output_html = 'html/simplenews.html'
    
class Aljazeera:
    _url   = ''
    _data  = ''
    _log  = None
    _soup  = None 
    
    def __init__(self, url, log):
        self._url  = url 
        self._log = log 
    
    def retrieve_webpage(self):
        try:
            html = urlopen(self._url)
        except Exception as e:
            print (e)
            self._log.report(str(e))
        else:
            self._data = html.read()
            if len(self._data) > 0:
                print ("Retrieved successfully")
            
    def write_webpage_as_html(self, filepath=raw_html, data=''):
        if data is '':
            data = self._data
        helper.write_webpage_as_html(filepath, data)
            
    def read_webpage_from_html(self, filepath=raw_html):
        self._data = helper.read_webpage_from_html(filepath)
            
    def change_url(self, url):
        self._url = url
            
    def print_data(self):
        print (self._data)
    
    def convert_data_to_bs4(self):
        self._soup = BeautifulSoup(self._data, "html.parser")
        
    def parse_soup_to_simple_html(self):
        news_list = self._soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # h1
        
        #print (news_list)
        
        htmltext = '''
<html>
    <head><title>Simple News Link Scrapper</title></head>
    <body>
        {NEWS_LINKS}
    </body>
</html>
'''
        
        news_links = '<ol>'
        
        for tag in news_list:
            if tag.parent.get('href'):
                # print (self._url + tag.parent.get('href'), tag.string)
                link  = self._url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)
                
        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        
        # print(htmltext)
        self.write_webpage_as_html(filepath=output_html, data=htmltext.encode())
    
    
    def print_beautiful_soup(self):
        # print (self._soup.title.string)
        news_list = self._soup.find_all(['h1', 'h2', 'h4']) # h1
        
        #print (news_list)
        for tag in news_list:
            if tag.parent.get('href'):
                print (self._url + tag.parent.get('href'), tag.string)
    
