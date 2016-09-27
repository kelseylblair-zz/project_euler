from common import get_divisors

upper_limit = 28123
abundant = []
total = 1

for x in xrange(2, upper_limit):
	if sum(get_divisors(x)) >= x:
		abundant.append(x)
	for y in abundant:
		if x-y in abundant:
			total += x
			break

print total

