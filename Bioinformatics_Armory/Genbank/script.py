#!/usr/bin/env python
# manipulate an inpute file to generate new file with some conditions

from Bio import Entrez
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
record["Count"]

# Sample input
# Dysstroma
# 2006/01/25
# 2012/10/25

# Actual query used handle = Entrez.esearch(db="nucleotide", term='"Dysstroma"[Organism]) AND ("2006/01/25"[Publication Date] : "2012/10/25"[Publication Date])')
# Answer: 435
