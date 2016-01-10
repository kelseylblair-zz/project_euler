# first find the triangle numbers
# then find the factors of the triangle numbers
# then count the factors
# find the first number that is a triangle that has over 500 divisors

from common import factorize
from itertools import combinations as combo

number = 0
count = 1
num_factors = 0
TARGET = 500

while num_factors <= TARGET:
	number += count
	num_factors = len(factorize(number))
	count += 1

print number, num_factors





# THIS IS TOO INEFFICIENT

# from common import prime_factors, product, factorize
# from itertools import combinations_with_replacement as combo

# TARGET = 5
# num_factors = 0
# factors = set([])
# number = 0 #triangle number
# count = 1 #size of factor combos
# index = 1 #triangle number counter

# while num_factors <= TARGET:
# 	num_factors = 0
# 	number += index
# 	factors = set(prime_factors(number))
# 	for x in factors:
# 		num_factors += 1
# 	for count in range(1, len(factors)+1):
# 		for x in combo(factors, count):
# 			temp = set(x)
# 			if(number % product(x) == 0):
# 				for element in x:
# 					if element not in factors:
# 						factors.add(element)
# 						num_factors += 1
# 				if product(x) not in factors:
# 					factors.add(product(x))
# 					num_factors += 1
# 	num_factors += 2
# 	index += 1

# print number, factorize(number)


# index = 1
# triangle = 0
# TARGET = 7
# factors = set()

# while len(factors) < TARGET:
# 	triangle = 0
# 	for x in xrange(1, index+1):
# 		triangle += x
# 	factors = factorize(triangle)
# 	index += 1


# print triangle, factors