# find multiples of 3
# find multiples of 5
# exclude double-counting of things that are both
# add

mult_3 = []
mult_5 = []
doubles = []
total = 0

for x in xrange(1, 1000):
	if x % 3 == 0:
		mult_3.append(x)
	if x % 5 == 0:
		mult_5.append(x)

for x in mult_3:
	if x % 5 == 0:
		doubles.append(x)
		mult_3.remove(x)
		mult_5.remove(x)

for x in mult_3:
	total += x
for x in mult_5:
	total += x
for x in doubles:
	total += x

print total