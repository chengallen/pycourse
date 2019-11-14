#!/usr/bin/env python3


vrange = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for row in vrange 
	for col in vrange:
		if col > row:
			break
		v = row * col

		print(f'{row}*{col} = {v}', end=' ')

	print('')


fd = open(r'd:\xiaowei.txt')

fd.read()

fd.close()

with open(r'd:\xiaowei.txt') as fd:
	for line in fd.readline():
		pass


import sqlite3

con = sqlite3.connect(':memory:')



DDL, DQL, DML, DCL

