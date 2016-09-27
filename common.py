from itertools import combinations

def factorial(number):
	answer = 1
	for x in xrange(1, number+1):
		answer *= x
	return answer


def factorize(number):
	index = 1
	factors = set([number, 1])

	primes = prime_factors(number)

	for x in primes:
		factors.add(x)
		number /= x

	for x in range(1, len(primes)):
		for y in combinations(primes, x):
			factors.add(product(y))

	return factors

def nth_fibonacci(limit):
	a = 1
	b = 1
	for x in xrange(limit):
		a, b = b, a + b
	return b		

def get_divisors(number):
        divisors = [1]
	if number > 1:
       		for x in xrange(2, number):
                	if number % x == 0 and x not in divisors:
                        	divisors.append(x)
                        	divisors.append(number / x)
		return divisors

def get_nth_prime(index):
	count = 1
	number = 2
	primes = []

	while count <= index:
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

	return answer

def is_prime(number):
	primes = sieve(number)
	if number < 2:
		return False
	return primes[-1] == number


def prime_factors(number):
	index = 2
	primes = []

	while number > 1:
		while number % index == 0:
			number /= index
			primes.append(index)
		index += 1

	return primes


def product(factors):
	answer = 1
	for x in factors:
		answer *= x
	return answer

def sieve(UPPER_BOUND):
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

	return primes

def sum_digits(number):
	total = 0
	for c in str(number):
		total += int(c)
	return total 
