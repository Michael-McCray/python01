name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
	handle= open(name)
except: 
	print "is not file"

hours = {}

for line in handle:
	if not line.startswith('from '):
		continue
	hours = line.split()
	time = hours [5]
	hour = time.split(:)
	hours[hour[0]] = hours.get(hour[0], 1) + 1 

print "\nHours & Counts"
print hours