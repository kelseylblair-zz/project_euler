f = open('input_008.txt', 'r')

str_number = ""
factors = [0] * 13
product = 1
index = 0
result = 1

for line in f:
	str_number += line.rstrip()

while index < 13:
	factors[index] = int(str_number[index])
	index += 1

while index < len(str_number):
	for y in factors:
		product *= y
	if product > result:
		result = product
	product = 1
	for x in range(12):
		factors[x] = factors[x+1]
	factors[12] = int(str_number[index])
	index += 1

print result







# for x in "1111119999111111":
# 	if index == 4:
# 		product = 1
# 		for y in factors:
# 			product *= y
# 		if product > answer:
# 			answer = product
# 			print answer
# 		for z in xrange(3):
# 			factors[z] = factors[z+1]
# 		index = 3
# 	else:
# 		factors[index] = int(x)
# 		index += 1
# 		print factors

#print answer