# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/webscraping
# blog: http://thinkdiff.net
# MIT License

# --------------------------
#  Data Parsing
# --------------------------

from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html_data = urlopen('http://www.bbc.com')
bs_obj = BeautifulSoup(html_data.read(), 'html.parser')

print(bs_obj.h1)
print(bs_obj.h1.string)