# prime factor input
# ---list of primes to mod against?
# compare prime factors to find largest

number = 600851475143
index = 2

while number > 1:
	while number % index == 0:
		number /= index
	index += 1

print index - 1


# for x in xrange(2, number/2 + 1):
# 	while number % x == 0:
# 		number = number / x
# 		factors.append(x)

# for x in factors:
# 	for y in xrange(2, x):
#  		if x != y and x % y == 0:
#  			prime = False
#  	if prime == True:
#  		prime_factors.append(x)	

# largest = prime_factors[-1]

# print largest

# for x in xrange(1, number):
# 	if number % x == 0:
# 		factors.append(x)

# for x in factors:
# 	for y in xrange(2, x):
# 		if x != y and x % y == 0:
# 			prime = False
# 	if prime == True:
# 		prime_factors.append(x)

# largest = prime_factors[-1]

# print largest


# THIS WAS TOO INEFFICIENT
# #create list of primes
# for x in xrange(2, number):
# 	for y in xrange(2, x):
# 		if x != y and x % y == 0:
# 			test.append(y)
# 	if not test:
# 		primes.append(x)
# 	test = []

# for x in primes:
# 	if number % x == 0:
# 		factors.append(x)

# largest = factors[-1]

# print largest	