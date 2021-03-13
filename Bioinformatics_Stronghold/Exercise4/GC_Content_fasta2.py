#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and prints out a reverse compliment

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO

x = raw_input("Enter File Name: ")
input_file = open(x, 'r') 
output_file = open('test2.txt','w') 
output_file.write('Gene\tCG%\n') 
for cur_record in SeqIO.parse(input_file, "fasta") :
	gene_name = cur_record.name
	A_count = cur_record.seq.count('A')
	C_count = cur_record.seq.count('C')
	G_count = cur_record.seq.count('G')
	T_count = cur_record.seq.count('T')
	length = len(cur_record.seq)
	cg_percentage = float(C_count + G_count) / length
	output_line = '%s\t%f\n' % \
	(gene_name, cg_percentage)
	output_file.write(output_line)
output_file.close()
input_file.close()



