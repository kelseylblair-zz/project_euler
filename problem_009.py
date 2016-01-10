# a^2 + b^2 = c^2
# a + b + c = 1000
# none of the numbers can be larger that 998

UPPER_LIMIT = 450

a = 1
b = 1
c = 1

for x in range(1, UPPER_LIMIT+1):
	for y in range(1, UPPER_LIMIT+1):
		for z in range(1, UPPER_LIMIT+1):
			if x**2 + y**2 == z**2 and x < y < z and x + y + z == 1000:
				a = x
				b = y
				c = z

print a * b * c