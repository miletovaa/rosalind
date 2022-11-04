# Counting DNA Nucleotides

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

s = 'ACTTGATCCTCACAAGGGGCAGGCCTAGCTGTTTAACAACGAAACGGTCTAGTTCTTTACCGGAAAGGGCAGCTTGACATGCTCCCCTGGATGTTGTATTGATTACAGTCATTGTGCAGGTTTAGTGTAAGACCGGATAACCGAGGCTACTAGATGGATCACCTCCTTTGCCCACCTCCTTTTCCCACAAAGGGGTCAACAATCATCTTCCGCTCGCAGCAGGATAGCTTGTAGCGTGGCTGTAGTCTCTTATTTCTCATACCAACAGATGAAAGTACCCTATTGATTGAATCCCCGGCGACGAGCTGCGCCTGATACAGTCGACAGTCAGAAGATCCTGCATGTGCCGCATGTTGTTCAGATGGAATGTAAATACCGCATTGACGCGCGACCCGCGTGTATCCCTAGTAACCTGTTGTCTTTTATTGATCAGTGGTCATTTATGGTTTCGTCCATCGAAAAATTAGTAGTCGAGCGAGATCTTTTATCAGTTATTGCTGAAGCATTAGTATATATGGAGTGTTTCATGACCATAGTTGAAGCGGCCCATCGCGCAGCAAGCTTCAAGATATACGTGTTTTCCACACACCGTCGATTTTCGGAAGGGTCGTATGAACTTCGGTGCGTTTGGACACGAATCGATAAAAGGAGATAGTTGAAAAAGTGTTACCGTCCGTAGCGACGGTTAACCTACTTGTCACGGGAATAAGACTACGCGTTGTGGCAAGGGGATGCAACGGCATGTGAGACAGTTCGATACAAGGCGCCTGCTTTAAGGGGATCGAACTCAAATTGGTGTAAAATAACCAACAAGGTATCGTAAGCTTATTAGGCCGTTTCTTCGTGAATTATTAA'

# 1
def qt(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

# 2
freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in s:
    freq[i] += 1
print(freq['A'], freq['C'], freq['G'], freq['T'])