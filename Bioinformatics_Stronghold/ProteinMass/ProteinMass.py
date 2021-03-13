#!/usr/bin/env python
# program takes Amino Acid Seq and calculates MW of the protein


from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import IUPACData
from Bio.SeqUtils.ProtParam import ProteinAnalysis

x = raw_input("Enter a AA sequence: ")
analysed_seq = ProteinAnalysis(x, monoisotopic=True)

y = analysed_seq.molecular_weight()

y
