fname = raw_input("Enter file name: ")

if len(fname) == 0:
	fname == 'mbox-short.txt'

try:
	fh= open(fname)
except: 
	print "is not file"

for line in fh:
	if not line.startswith('X-DSPAM-Confidence:    0.8475'):
		continue
	
	num_start = line.find('0')
	num = line[num_start]
	flt = float(num)
	count += flt

print count