from itertools import permutations 
from common import factorial

SIZE = 20
path_size = SIZE * 2
directions = (["R"] * SIZE + ["D"] * SIZE)
routes = []
num_routes = 0

#permutations of R and D of length path_size such that each 
#permutation includes exactly as many instances of R or D as SIZE

#permutations = n!/(n-k)!



print len(routes)
