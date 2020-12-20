# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:31:57 2020

@author: Andrew
"""

import re

fName = 'input.txt'

# Part 1 and loading the data to a dict
fp = open(fName,'r')
pptList = []
keys = []
vals = []
valids = 0
p = ''
s = fp.readline()
while (s != ''):
  if s == '\n':
    tmp = p.split(' ')[:-1]
    for el in tmp:
      k,v = el.split(':')
      keys.append(k)
      vals.append(v)
    tmpDict = dict(zip(keys,vals))
    pptList.append(tmpDict)
    if len(keys)==8:
      valids += 1
    elif (len(keys)==7 and 'cid' not in keys):
      valids += 1
    keys = []
    vals = []
    p = ''
  else:
    s = s.replace('\n', ' ')
    p += s
  s = fp.readline()
tmp = p.split(' ')
for el in tmp:
  k,v = el.split(':')
  keys.append(k)
  vals.append(v)
tmpDict = dict(zip(keys,vals))
pptList.append(tmpDict)
if len(keys)==8:
  valids += 1
elif (len(keys)==7 and 'cid' not in keys):
  valids += 1
fp.close()
print("Part 1 Answer: Number of Valid IDs = {0}".format(valids))

# Part 2
valids = 0
goodEyeCol = ['amb','blu','brn','gry','grn','hzl','oth']
for d in pptList:
  keys = d.keys()
  if (len(keys)<7):
    continue
  elif (len(keys)==7 and 'cid' in keys):
    continue
  # Birth year check
  if int(d['byr']) <1920 or int(d['byr']) > 2002:
    continue
  # Issue year check
  if int(d['iyr']) < 2010 or int(d['iyr']) > 2020:
    continue
  # Expiration year check
  if int(d['eyr']) < 2020 or int(d['eyr']) > 2030:
    continue
  # Height check
  hstr = d['hgt']
  if 'cm' in hstr:
    h = int(hstr[:hstr.find('cm')])
    if h < 150 or h > 193:
      continue
  elif 'in' in hstr:
    h = int(hstr[:hstr.find('in')])
    if h < 59 or h > 76:
      continue
  else:
    continue
  # Hair color check
  patt = '\#[\da-f]{6}'
  if len(d['hcl'])!=7:
    continue
  elif not bool(re.match(patt,d['hcl'])):
    continue
  # Eye color check
  if len(d['ecl']) != 3:
    continue
  elif d['ecl'] not in goodEyeCol:
    continue
  # Passport ID Check
  if len(d['pid']) != 9 or not d['pid'].isnumeric():
    continue
  # All checks passed, count it as valid
  valids += 1
print("Part 2 Answer: Number of Valid IDs = {0}".format(valids))
  