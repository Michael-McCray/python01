import urllib 
from BeautifulSoup import * 

url = raw_input(" URL: ")
count = raw_input(" count: ")
position = raw_input(" position: ")
 
count = int(count)
position = int(position)

while count > 0:
	links = [] 
	tags = BeautifulSoup(urllib.urlopen(url).read())('a')
	
	for tag in tags:
		links.append(tag.get('href', None))

	url = links[position-1]
	count -= 1 

print url
