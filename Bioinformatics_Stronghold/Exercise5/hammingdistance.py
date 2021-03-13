#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and prints out a reverse compliment

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO

def hamming_distance(s1, s2) :
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
	
if __name__=="__main__":
	a = raw_input("Enter Sequence 1: ")
	b = raw_input("Enter Sequence 2: ")
	print hamming_distance(a, b)

