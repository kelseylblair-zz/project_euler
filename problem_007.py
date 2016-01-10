from common import prime_factors

count = 1
number = 2
primes = []

while count <= 10001:
	isprime = True
	for x in primes:
		if number % x == 0:
			isprime = False
			break
	if isprime == True:
		answer = number
		count += 1
		primes.append(number)
	number += 1

print answer, count - 1