# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:33:24 2020

@author: Andrew
"""

# Get file input
fName = 'input.txt'
with open(fName,'r') as fp:
  mapList = fp.readlines()

# PART 1
# Traversal sizes
stepX = 3
# Get total number of Y levels to cover 
totalY = len(mapList)
# Get total number of X levels before wrapping (each string is equal length)
totalX = len(mapList[0].strip('\n'))
# Set the counters
cntOpen = 0
cntTree = 0
# Iterate through the map using Rise/Run = 1/stepX and count # of trees and open spaces encountered
xPos = 0
for s in mapList:
  # Since the calculated length of string excluded the newline character, we don't have to strip it here (we'll wrap)
  if(s[xPos] == '.'):
    cntOpen += 1
  else:
    cntTree += 1
  # Update x-position
  xPos = (xPos+stepX)%totalX
# Print answer
print("Part 1 Answer: Trees Encountered = {0}".format(cntTree))

# PART 2
# Traversal sizes
stepX = [1,3,5,7,1]
stepY = [1,1,1,1,2]
# Set the counters
cntTree = [0,0,0,0,0]
prodTree = 1
# Iterate through each slope scenario, counting the number of trees encountered on each slope
for i in range(len(stepX)):
  # Reset x-position
  xPos = 0
  # Iterate through the map
  for yPos in range(0,totalY,stepY[i]):
    # Get the current map string
    s = mapList[yPos]
    # Since the calculated length of string excluded the newline character, we don't have to strip it here (we'll wrap)
    if(s[xPos] == '#'):
      cntTree[i] += 1
    # Update x-position
    xPos = (xPos + stepX[i])%totalX
  # Print number of trees on this path
  print("Path {0} Trees: {1}\n".format(i,cntTree[i]))
  # Calculate running product
  prodTree = prodTree * cntTree[i]
# Print Answer
print("Part 2 Answer: Product of Trees Encountered = {0}".format(prodTree))