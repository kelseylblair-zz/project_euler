# start with 999 x 999 and increment down
# first check to see if its a palindrome
# then check to see if it's divisible by three digit numbers counting up

start = 999 * 999
end = 100 * 100
string = ""

for x in xrange(start, end, -1):
	string = str(x)
	if string[0] == string[-1] and string[1] == string[-2] and string[2] == string[-3]:
		for y in xrange(100, 999):
			if x % y == 0 and x / y <= 999:
				print x
				exit()

