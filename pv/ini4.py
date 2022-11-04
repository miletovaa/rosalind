# Conditions and Loops

# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

s = 0
a = 4738
b = 8758

while a<b:
	if a%2 == 1:
		s = s+a
	a = a+1

print(s)