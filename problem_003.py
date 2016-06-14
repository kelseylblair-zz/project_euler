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