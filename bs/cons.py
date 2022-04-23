# Consensus and Profile

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)


# 1
strings = [] # массив ДНК-строк из файла, где каждая строка - побуквенный массив
with open('input/rosalind_cons.txt') as fasta:
    for line in fasta:
        if len(line) > 1:
            if 'Rosalind' in line:
                strings.append([])
            else:
                line = line.strip()
                for l in line:
                    strings[-1].append(l)

profile = []
for col in list(zip(*strings)):
    profile.append([0,0,0,0])
    for l in col:
        match l:
            case 'A':
                profile[-1][0] += 1
            case 'C':
                profile[-1][1] += 1
            case 'G':
                profile[-1][2] += 1
            case 'T':
                profile[-1][3] += 1

consensus = ''
i = 0
for col in profile:
    consensus += 'A' if max(col) == col[0] else 'C' if max(col) == col[1] else 'G' if max(col) == col[2] else 'T'
    i+=1
print(consensus)

transpose = [list(i) for i in zip(*profile)]
print('A:',' '.join(str(x) for x in transpose[0]))
print('C:',' '.join(str(x) for x in transpose[1]))
print('G:',' '.join(str(x) for x in transpose[2]))
print('T:',' '.join(str(x) for x in transpose[3]))


# 2
strings = [] # массив ДНК-строк из файла, где каждая строка - побуквенный массив
with open('input/rosalind_cons.txt') as fasta:
    for line in fasta:
        if len(line) > 1:
            if 'Rosalind' in line:
                strings.append([])
            else:
                line = line.strip()
                for l in line:
                    strings[-1].append(l)

profile = []; profile_l = []
for col in list(zip(*strings)):
    profile.append({'A':0,'C':0,'G':0,'T':0})
    for l in col:
        profile[-1][l] += 1

for col in profile:
    row = {}
    profile_l.append([])
    for key, value in col.items():
        row[value] = key
        profile_l[-1].append(value)
    print(row[max(row)], end='')
print('\n')

i = 0
for k in list(zip(*profile_l)):
    n = 'A:' if i == 0 else 'C:' if i == 1 else 'G:' if i == 3 else 'T:'
    print(n,' '.join(str(x) for x in k))
    i += 1