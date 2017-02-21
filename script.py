import urllib2
import requests
from bs4 import BeautifulSoup

url = 'http://www.86kongqi.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request, timeout=20)

content = response.read()
soup = BeautifulSoup(content, 'html.parser')

tag = soup.body.dl
children = tag.children

for child in children:
	print child

