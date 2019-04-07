#!/usr/bin/env python

import sys
import json

for line in sys.stdin:
  print json.loads(line)['business_id'],1

