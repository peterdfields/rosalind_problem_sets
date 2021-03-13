#!/usr/bin/env python
# extract text from string given positions a, b, c, and d

s = raw_input("Enter string: ")
a = raw_input("Enter position a: ")
b = raw_input("Enter position b: ")
c = raw_input("Enter position c: ")
d = raw_input("Enter position d: ")

print ('The statement is ____{} {}'.format(s[int(a):(int(b)+1)], s[int(c):(int(d)+1)]))
