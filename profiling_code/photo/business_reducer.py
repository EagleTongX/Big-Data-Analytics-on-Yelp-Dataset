#!/usr/bin/env python

import sys

output={}

for line in sys.stdin:
  key,value=line.split()[0],line.split()[1]
  if key not in output:
    output[key]=1
  else:
    output[key]+=1

for i in output:
  print i,output[i]
