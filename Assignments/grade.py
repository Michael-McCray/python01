score = raw_input("Enter Score: ")
s= float(score)
def grade(s):
	if s >= 0.9: 
		return 'A'
	elif s >= 0.8: 
		return 'B'
	elif s >= 0.7: 
		return 'C'
	elif s >= 0.6: 
		return 'D'
	elif s < 0.6: 
		return 'F'
	elif s > 1.0:
		return 'error'
	elif s < 0.0:
		return 'error'
	else: 
		return "no score"
print grade(s)