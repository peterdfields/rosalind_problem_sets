#!/usr/bin/env python
# program calculates number of individuals with dominant phenotype

from __future__ import division

k = raw_input("Enter # of Homozygote Dominant Individuals: ")
m = raw_input("Enter # of Heterozygote Dominant Individuals: ")
n = raw_input("Enter # of Homozygote Recessive Individuals: ")

k = int(k)
m = int(m)
n = int(n)

o = k+m+n

w = ((m / o) * ((m - 1) / (o - 1))) * (1 / 4)
x = ((m/o)*((n)/(o-1)))*(1/2)

y = ((n/o)*((m)/(o-1)))*(1/2)
z = ((n/o)*((n-1)/(o-1)))

N = (w+x+y+z)
A = 1-N

print A


