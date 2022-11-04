# Enumerating Gene Orders

# Given: A positive integer n≤7
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

from itertools import permutations

n = int(input())

comb_num = 0
list = []
i = 1

while i != n+1:
	list.append(str(i))
	i +=1

for i in permutations(list, ):
    print(' '.join(i))
    comb_num += 1

print(comb_num)