def compute_pay(rate, hours):
	try: 
		rate = float(rate)
		hours = float(hours)
	except:
		print "these need to be numbers"
	if hours > 40:
		extra_hours = hours - 40
		extra_pay = rate * 1.5
		total = (rate * 40)+ (extra_pay	* extra_hours)
		return total
	else:
	total = rate* hours
	return total	

p =	Compute_pay( 10,20 )
print p 