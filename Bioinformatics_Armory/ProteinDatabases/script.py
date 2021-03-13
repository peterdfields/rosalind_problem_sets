#!/usr/bin/env python
# manipulate an inpute file to generate new file with some conditions

from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('B5ZC00') #you can give a several ID divided by comma
record = SwissProt.read(handle) # SwissProt.parse for the several proteins

print record.cross_references

# The correct answer is to identify those descriptions that occur after "P:"

# sample given = P03568

# correct answer

# DNA replication
# modulation by virus of host G1/S transition checkpoint
# nucleic acid phosphodiester bond hydrolysis

