#!/usr/bin/env python
"""reviewReducer.py"""

import sys

final_output = {}

# aggregate the total number of reviews for each business
for line in sys.stdin:
    key,value = line.split()[0],line.split()[1]
    if key not in final_output:
      final_output[key] = 1
    else:
      final_output[key] = final_output[key] + 1

for i in final_output:
    print i,final_output[i]
