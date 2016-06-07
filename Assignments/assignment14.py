import urllib 
import xml.etree.ElementTree as ET 

while True:
	url = raw_input("Enter URL: ")
	if len(url) < 1 : break 
	total = 0 
	for comment in ET.fromstring(urllib.urlopen(url).read()).findall('comments/comment'): 
		total += int(comment.find('count').text)
	print total 