number = 1
longest = 0
TARGET = 1000000
answer = 0

chains = {}

while number <= TARGET:
	n = number
	num_terms = 0
	while n != 1:
		if n in chains:
			num_terms += chains[n]
			break
		elif n % 2 == 0:
			n /= 2
			num_terms += 1
		else:
			n = 3*n + 1
			num_terms += 1
	if n == 1:
		num_terms += 1
	if num_terms > longest:
		longest = num_terms
		answer = number
		
	chains[number] = num_terms

	number += 1

print answer

