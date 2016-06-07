fname = raw_input("Enter file name: ")
if len(fname) == 0:
	fname == 'romeo.txt'
try:
	fh= open(fname)
except: 
	print "is not file"

words = []

for line in fh:
	line_words= line.split()
	for word in line_words:
		if word in words:
			continue
			word.appened(word)

print sorted(words)

	