from common import factorial

n = 100
sum = 0
fact_n = factorial(n)
for digit in str(fact_n):
    sum += int(digit)
print sum
