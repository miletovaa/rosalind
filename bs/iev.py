# Calculating Expected Offspring

# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
# 	1 AA-AA
# 	2 AA-Aa
# 	3 AA-aa
# 	4 Aa-Aa
# 	5 Aa-aa
# 	6 aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

gen = '17209 18036 16323 19799 19530 17945'

k = i = 1
genot = {}
for g in gen.split(' '):
	genot[k] = g
	k += 1

expect = 0
for key in genot:
	value = int(genot[key]) * 2
	if key <= 3:
		expect += value
	elif key == 4:
		expect += value * 0.75
	elif key == 5:
		expect += value * 0.5
print(expect)