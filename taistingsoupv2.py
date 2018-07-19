import urllib2
from bs4 import BeautifulSoup

def url_to_soup(url):
    req = requests.get(url)
    return BeautifulSoup(req.content, 'html.parser')
    
def horse_page_link(url):
    soup = url_to_soup(url)
    link_list = [HOME_URL + x.get('href') for x in soup.find_all('a', class_='tx-mid tx-low') ]
    return link_list
