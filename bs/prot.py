# Translating RNA into Protein

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

codon_to_amino = {
	'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
	'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
	'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
	'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
	'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
	'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
	'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
	'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
	'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
	'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
	'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
	'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
	'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
	'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
	'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
	'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

codons_str = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
codon = aminos_str = ''
i = 1
for l in codons_str:
	if i%3 == 0:
		codon += l
		if codon_to_amino[codon] != 'Stop':
			aminos_str += codon_to_amino[codon]
		codon = ''
	else:
		codon += l
	i+=1

print(aminos_str)