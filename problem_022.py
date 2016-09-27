f = open('input_022.txt', 'r').read()
names = f.strip().split(',')
count = 1
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total = 0
sum = 0
score = 0

for name in sorted(names):
	name = name.strip('"')
	print name
	for x in xrange(len(name)):
		letter = name[x]
		sum += alphabet.index(letter) + 1
	score = sum * count
	total += score
	score = 0
	sum = 0
	count += 1

print total 
