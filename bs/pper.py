# Partial Permutations

# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
# Return: The total number of partial permutations P(n,k), modulo 1,000,000.

import math

n = 80
k = 9

print(int(math.factorial(n) / math.factorial(n-k)%1000000))