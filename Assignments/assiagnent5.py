largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num = "done" : break
    try:
    	num = int(num)
    except:
    	print "not a number"
    	continue
	if largest is none:
		largest = value
	elif value > largest:
		largest = value
		continue
	elif smallest is none:
		smallest = value
	elif value < smallest:
		smallest = value
		continue
print "Maximum", largest
print "minimum", smallest