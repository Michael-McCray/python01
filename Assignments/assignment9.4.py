name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
	handle= open(name)
except: 
	print "is not file"

emails = {}
email_list =[]

for line in handle:
	if not line.startswith('from '):
		continue
	email_list = line.split()
	email = words[1]
	email_list.appened(email)
	
for adress in email_list:
	email[adress] = emails.get(adress,0)+1

big_adress = None
big_number = None

for adress,count in emails.item():
	if big_count is None or count > big_count:
		big_count = count
		big_adress= adress
print big_adress,big_count