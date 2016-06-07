fname = raw_input("Enter file name: ")

if len(fname) == 0:
	fname == 'mbox-short.txt'

try:
	fh= open(fname)
except: 
	print "is not file"

count = 0

for line in fh:
	if not line.startswith('from '):
		continue
	words_list = line.split()
	email = words_list[1]
	count += 1
	print email

print count
