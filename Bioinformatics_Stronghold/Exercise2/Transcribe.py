#!/usr/bin/env python
# program calculates number of individuals with dominant phenotype


k = raw_input("Enter # of Homozygote Dominant Individuals: ")
m = raw_input("Enter # of Heterozygote Dominant Individuals: ")
n = raw_input("Enter # of Homozygote Recessive Individuals: ")
o = k+m+n

a1 = ((m/o)*((m-1)/(o-1)))*(1/4)
a2 = ((m/o)*((n)/(o-1)))*(1/2)

b1 = ((n/o)*((m)/(o-1)))*(1/2)
b2 = ((n/o)*((n-1)/(o-1)))

n1 = (a1+a2+b1+b2)
A = 1-n1

print A


