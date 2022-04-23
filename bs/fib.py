# Rabbits and Recurrence Relations

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n = 29 # amount of months
k = 5 # pairs per month

# 1
def fib(n):
	if n in(1,2):
		return 1
	return fib(n-1)+fib(n-2)*k
print(fib(n))

# 2
fibo = [1,1]
[fibo.append(k*fibo[-2]+fibo[-1]) for i in range(n-2)]
print(fibo[-1])