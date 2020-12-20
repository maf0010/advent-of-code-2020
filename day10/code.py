# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:09:39 2020

@author: Andrew
"""

import numpy as np

fName = 'input.txt'

# PART 1
k = np.loadtxt(fName,dtype=np.uint32)
k.sort()
k2 = np.append(np.array([0]),k)
k3 = np.append(k2,k2[-1]+3)
k4 = k3[1:] - k3[:-1]
uniques = np.unique(k4)
outArr,bins = np.histogram(k4,bins=len(uniques))
for i,u in enumerate(uniques):
  print("Number of {0}s in Array is {1}\n".format(u,outArr[i]))
  if u==1:
    ones = outArr[i]
  elif u==3:
    threes = outArr[i]
ans = ones * threes
print("Part 1 Answer is {0}\n".format(ans))

# PART 2
last = [0]
paths = [1]
for el in k:
  sVal = 0
  for i in range(1,3+1):
    if (el-i) in last:
      sVal += paths[last.index(el-i)]
  if len(last)==3:
    last.pop(0);
    paths.pop(0);
  last.append(el)
  paths.append(sVal)
ans2 = sVal
print("Part 2 Answer is {0}\n".format(ans2))