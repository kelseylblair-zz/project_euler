answer = 0

with open("input_013.txt", "r") as num_file:
	for line in num_file:
		answer += int(line)

str_answer = str(answer)

print str_answer[:10]
