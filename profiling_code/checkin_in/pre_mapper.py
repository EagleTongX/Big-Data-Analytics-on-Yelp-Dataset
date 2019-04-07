#!/usr/bin/env python
import json
import sys

words=('Fri','Sat','Sun')

for line in sys.stdin:
	data= json.loads(line)
	rest= data['business_id']
	for key in data['time']:
		weekday=key.split("-")[0]
		count=data['time'][key]
		for word in words:
			if word in weekday:
				print '%s\t%s' % (rest+'-'+word, count)




