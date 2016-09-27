from common import sum, get_divisors

upper_limit = 10000
amicable = []

for x in xrange(1, upper_limit):
	d = sum(get_divisors(x))
	if d != 0 and sum(get_divisors(d)) == x:
		if x != d:
			if x not in amicable:
				amicable.append(x)
			if d not in amicable:
				amicable.append(d)
print amicable
print sum(amicable) 

