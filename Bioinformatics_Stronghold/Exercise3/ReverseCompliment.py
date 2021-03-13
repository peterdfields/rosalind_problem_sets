#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and prints out a reverse compliment

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

x = raw_input("Enter a DNA sequence: ")
x = Seq(x, generic_dna)

m = x.reverse_complement()

print m


