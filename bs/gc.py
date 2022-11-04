# Computing GC Content

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

dna_strings = {}
with open('input/rosalind_gc.txt') as fasta:
    for line in fasta:
        if len(line) > 1:
            if 'Rosalind' in line:
                key = line.strip()
                dna_strings[key] = ""
            else:
                dna_strings[key] += line.strip()

dict = {key: dna_strings[key] for key in dna_strings}

cg_content ={}

for key, dna in dna_strings.items():
	cg = (dna.count('C') + dna.count('G'))/ len(''.join(dna.splitlines()))*100
	cg_content[key] = cg

max_val = max(cg_content.values())
max_key = ''

for key, value in cg_content.items():
	if value == max_val:
		max_key = key

print(max_key[1:])
print(max_val)