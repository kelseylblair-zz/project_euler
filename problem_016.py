# 2^15 = 32768 and the sum of digits = 26
# solve for 2^1000

from common import sum_digits

BASE = 2
EXPONENT = 1000

print sum_digits(BASE**EXPONENT)