hours = raw_input ("Enter Hours: ")
rate = raw_input ("Enter Rate: ")
h = float(hours)
r = float(rate)
if h > 40:
	  overtimeRate = 1.5 * r
	  overtime = (h-40) * overtimeRate
	  h = 40
	  pay = h * r + overtime
	  print pay
else:
  	overtime = 0
	pay = h * r + overtime
	print pay