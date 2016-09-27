lower = 2
upper = 100
terms = []

for a in xrange(lower, upper + 1):
	for b in xrange(lower, upper + 1):
		temp = a**b
		if temp not in terms:
			terms.append(temp)	

print len(terms)
