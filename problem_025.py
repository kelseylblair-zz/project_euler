a = 1
b = 1
count = 2
limit = 1000

while(len(str(b)) < limit):
	a, b = b, a+b
	count += 1

print count


