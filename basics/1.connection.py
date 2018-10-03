# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/webscraping
# blog: http://thinkdiff.net
# MIT License

# --------------------------
#  Connection
# --------------------------

from urllib.request import urlopen 

html_data = urlopen('http://www.google.com')
print(html_data.read())