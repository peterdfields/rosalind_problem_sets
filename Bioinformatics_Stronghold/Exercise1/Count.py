#!/usr/bin/env python
# program takes a DNA sequence (without checking)
# and shows its length and the nucleotide composition

DNASeq = "ATGAAC"
DNASeq = raw_input("Enter a DNA sequence: ")
DNASeq = DNASeq.upper() # convert to uppercase for .count() function
DNASeq = DNASeq.replace(" ","") # remove spaces

print 'Sequence:', DNASeq

SeqLength = float(len(DNASeq))

print "Sequence Length:", SeqLength

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

A_str = str(NumberA)
C_str = str(NumberC)
G_str = str(NumberG)
T_str = str(NumberT)



print A_str+" "+C_str+" "+G_str+" "+T_str
