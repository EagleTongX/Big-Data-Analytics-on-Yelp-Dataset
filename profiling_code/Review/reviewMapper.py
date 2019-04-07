#!/usr/bin/env python
"""reviewMapper.py"""

import sys
import json

for line in sys.stdin:
    print json.loads(line)['business_id'], 1
