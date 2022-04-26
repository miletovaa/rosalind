# Enumerating k-mers Lexicographically

# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

import itertools

inp = 'A B C D E F G H'
n = 4 # длина каждой необходимой строки
string = inp.replace(' ', "")

[print(''.join(x)) for x in itertools.product(*[string], repeat=n)]