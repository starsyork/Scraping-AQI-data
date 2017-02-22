import urllib2
import requests
import re
from bs4 import BeautifulSoup


def getSoup(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request, timeout=20)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup


re1='.*?'	# Non-greedy match on filler
re2='".*?"'	# Uninteresting: string
re3='.*?'	# Non-greedy match on filler
re4='".*?"'	# Uninteresting: string
re5='.*?'	# Non-greedy match on filler
re6='".*?"'	# Uninteresting: string
re7='.*?'	# Non-greedy match on filler
re8='".*?"'	# Uninteresting: string
re9='.*?'	# Non-greedy match on filler
re10='".*?"'	# Uninteresting: string
re11='.*?'	# Non-greedy match on filler
re12='".*?"'	# Uninteresting: string
re13='.*?'	# Non-greedy match on filler
re14='(".*?")'	# Double Quote String 1
pattern = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re14,re.IGNORECASE|re.DOTALL)

re15='.*?'	# Non-greedy match on filler
re16='(?:[a-z][a-z]+)'	# Uninteresting: word
re17='.*?'	# Non-greedy match on filler
re18='((?:[a-z][a-z]+))'	# Word 1
rg = re.compile(re15+re16+re17+re18,re.IGNORECASE|re.DOTALL)

d = {}

url = 'http://www.86kongqi.com'
soup = getSoup(url)
# To reduce the run time, I just get the first <dd> tag element.
tags = soup.body.dl.dd.find_all('a')
for tag in tags:
    # print tag['href']
    m = rg.search(tag['href'])
    if m:
        city=m.group(1)

    nexturl = url + '/' + tag['href']
    bs = getSoup(nexturl)
    script = bs.body.find("script", text=pattern)
    # print script
    match = pattern.search(script.text)
    if match:
        idx = match.group(1)
        # print "aqi" + idx
    d[city] = idx
print d
