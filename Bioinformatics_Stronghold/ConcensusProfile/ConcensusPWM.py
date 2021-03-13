#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and prints out a reverse compliment

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO
from Bio import Motif
from Bio.Alphabet import IUPAC

m = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
x = raw_input("Enter File Name: ")
m.add_instance(Seq(x,m.alphabet))
 
print m.consensus()



