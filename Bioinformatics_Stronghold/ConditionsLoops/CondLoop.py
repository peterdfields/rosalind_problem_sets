#!/usr/bin/env python
# manipulate an inpute file to generate new file with some conditions

a raw_input("Enter File Name: ")
b = open('input.txt', 'r')
c = open('output.txt', 'w')

d = 0
if d + 1 == 1:
		c = c + a
		a = a + 1
	else:
		a = a + 1

print c
