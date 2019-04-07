#!/usr/bin/env python
import json
import sys

for line in sys.stdin:
	data = json.loads(line)
	rest = data['business_id']
	for key in data['time']:
		num = data['time'][key]
		print '%s\t%s' % (rest, num)

