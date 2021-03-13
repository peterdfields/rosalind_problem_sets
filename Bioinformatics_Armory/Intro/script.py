#!/usr/bin/env python
# manipulate an inpute file to generate new file with some conditions


from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")

my_seq.count("A")
my_seq.count("C")
my_seq.count("G")
my_seq.count("T")



