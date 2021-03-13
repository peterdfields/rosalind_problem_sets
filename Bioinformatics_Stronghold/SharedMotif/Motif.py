#!/usr/bin/env python
# Find longest shared motif

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

clean = open('rosalind_lcs.txt').read().replace('\n', ",")
clean = clean[:-1]
clean = clean.split(',')


print long_substr(clean)






#analysed_seq = ProteinAnalysis(x, monoisotopic=True)

#y = analysed_seq.molecular_weight()

#y
