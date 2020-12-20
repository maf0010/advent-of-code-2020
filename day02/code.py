# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:13:24 2020

@author: Andrew
"""

fName = 'input.txt'

# Part 1

# Open the file and get the data
with open(fName,'r') as fp:
  dataList = fp.readlines()

# Iterate through each password & criteria
valids = 0
for s in dataList:
  # Remove newline character
  s = s.strip('\n')
  # Split into the criteria string and password
  tmp = s.split(": ")
  sub = tmp[0]
  p = tmp[1]
  # Get the criteria character
  c = sub[-1]
  # Get the minmax criteria
  m = [int(el) for el in sub[:-2].split('-')]
  # Get count of criteria character in the password
  cnt = p.count(c)
  # If count is between min/max criteria, password is valid
  if (cnt>=m[0]) and (cnt<=m[1]):
    valids += 1
# Report
print("Part 1 Answer: Number of valid passwords is {0}\n".format(valids))


# Part 2
# Iterate through each password & criteria
valids = 0
for s in dataList:
  # Remove newline character
  s = s.strip('\n')
  # Split into the criteria string and password
  tmp = s.split(": ")
  sub = tmp[0]
  p = tmp[1]
  # Get the criteria character
  c = sub[-1]
  # Get the character criteria
  m = [int(el) - 1 for el in sub[:-2].split('-')]
  # Get the character at each position in the password and verify criteria character occurs only once at each position
  if (c==p[m[0]]) ^ (c==p[m[1]]):
    valids += 1
# Report
print("Part 2 Answer: Number of valid passwords is {0}\n".format(valids))
