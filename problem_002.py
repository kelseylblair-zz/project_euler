# generate sequence up to 4 million exclusive
# --- each term is the sum of the two previous
# --- track indexes?
# parse out even terms
# add

fibonnaci = [1, 2]
x = 1
y = 2
UPPER_BOUND = 4000000
total = 0

while (x + y) < UPPER_BOUND:
	new_term = x + y
	fibonnaci.append(new_term)
	x = y
	y = new_term

for x in fibonnaci:
	if x % 2 == 0:
		total += x

print total