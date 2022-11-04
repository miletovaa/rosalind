# Rabbits and Recurrence Relations

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n = 29 # amount of months
k = 5 # pairs per month

def fib(n):
	if n in(1,2):
		return 1
	return fib(n-1)+fib(n-2)*k
print(fib(n))