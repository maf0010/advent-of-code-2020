# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:38:30 2020

@author: Andrew
"""

import numpy as np

# PART 1
fName = 'input.txt'
k = np.loadtxt(fName,dtype=np.int32)
goalSum = 2020
k2 = goalSum - k
answerVal = []
for i,el in enumerate(k2):
  if el in k:
    print("Location: {0}; Value: {1}\n".format(i,el))
    answerVal.append(el)

product = answerVal[0] * answerVal[1]
print("Part 1 Answer is {0}".format(product))


# PART 2
k3 = k2 - k.min()
for i,partSum in enumerate(k2):
  if (k3[i]<=0): # Toss any negatives
    continue
  tmp = partSum - k
  prt2Ans = []
  for el in tmp:
    if el in k:
      print("Value is {0}\n".format(el))
      prt2Ans.append(el)
  if len(prt2Ans) == 2:
    prt2Ans.append(k[i])
    break
  else:
    prtAns = []

prod2 = prt2Ans[0] * prt2Ans[1] * prt2Ans[2]
print("Part 2 Values are {0},{1},{2}\n".format(*prt2Ans))
print("Part 2 Answer is {0}\n".format(prod2))