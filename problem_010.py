UPPER_BOUND = 2000000
full_set = set([])
dict_set = {}
primes = []


for x in xrange(2, UPPER_BOUND+1):
	full_set.add(x)
	dict_set[x] = True

for x in full_set:
	if dict_set[x]:
		primes.append(x)
		for z in xrange(x**2, UPPER_BOUND+1, x):
			dict_set[z] = False

print sum(primes)









