# Mendel's first law
# Mendel's maxim that every gene has two alleles, one of which derives from each parent.

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k = 30 # AA
m = 18 # Aa
n = 18 # aa

print( (k*(k-1) + 0.75*m*(m-1) + 0.5*2*m*n + 2*k*m + 2*k*n) / ( (k + m + n)*(k + m + n-1) ) )