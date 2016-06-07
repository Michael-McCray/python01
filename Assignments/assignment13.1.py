import urllib 
from BeautifulSoup import * 
num = [] 
for tag in BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_242237.html').read())('span'):
	num.append(tag.contents[0])
	int(num)
print sum(num)