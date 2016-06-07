import urllib
import json

while True:
	url = raw_input('\nEnter location: ')
	if len(url) < 1 : break

	print 'Retrieving', url
	print '\nRetrieved',len(urllib.urlopen(url).read()),'characters'
	print 'Count:', len(json.loads(urllib.urlopen(url).read())['comments'])

	total = 0 
	for num in json.loads(urllib.urlopen(url).read())['comments']:
		total += int(num['count'])
	print 'Sum:', total