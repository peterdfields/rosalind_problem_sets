#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and prints out a reverse compliment

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO
from Bio.SeqUtils import GC

x = raw_input("Enter File Name: ")
y = open(x)
for seq_record in SeqIO.parse(y, "fasta") :
    print seq_record.id
    print len(seq_record)
y.close()



