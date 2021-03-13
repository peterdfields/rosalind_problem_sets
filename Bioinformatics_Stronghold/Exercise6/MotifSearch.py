#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and prints out a reverse compliment

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO
from Bio import Motif
from Bio.Alphabet import IUPAC
	
m = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
x = raw_input("Enter Sequence Motif: ")
m.add_instance(Seq(x,m.alphabet))


y = raw_input("Enter Sequence: ")
test_seq=Seq(y,m.alphabet)

for pos,seq in m.search_instances(test_seq):
	print pos+1,seq.tostring()
