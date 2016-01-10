# find sum of squares
# find square of sums
# subtract

numbers = xrange(1, 101)
squares = 0
sums = 0

for x in numbers:
	squares += (x*x)
	sums += x

sums *= sums

answer = sums - squares

print answer
