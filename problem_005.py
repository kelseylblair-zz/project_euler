# set of divisors
# start with 2520, count up
# or, start with 2520 and multiply by all the remaining divisors? 
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# list of odd numbers, also 2?

from common import primes

full_set = range(1, 21)
test = []
temp= []
divisors = []
answer = 1

for x in full_set:
	test = primes(x)
	temp = divisors[:]
	for y in test:
		if y in temp:
			temp.remove(y)
		else:
			divisors.append(y)
	print x, divisors

for x in divisors:
	answer *= x

print answer 

# def check_divisors(number):
# 	divisors = xrange(1, 11)
# 	works = True
# 	for x in divisors:
# 		if number % x != 0:
# 			works = False 
# 	if works == True:
# 		return number
# 	else:
# 		return 0

# number = 2520
# answer = 0

# while answer == 0:
# 	answer = check_divisors(number)
# 	number += 1

# print answer


