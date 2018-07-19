import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://www.yahoo.co.jp/")

soup = BeautifulSoup(html, "html.parser")
print(soup.title) 
