from itertools import permutations 
from common import factorial

SIZE = 20
num_routes = factorial(2 * SIZE) / (factorial(SIZE)**2)

print num_routes
