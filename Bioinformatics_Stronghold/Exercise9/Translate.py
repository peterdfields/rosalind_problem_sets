#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and shows its length and the nucleotide composition

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_rna
from Bio import SeqIO

x = open("rosalind_prot.txt")
lines = x.readline()
y = Seq(lines, generic_rna)

m = y.translate()

print m
