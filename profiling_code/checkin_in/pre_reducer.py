#!/usr/bin/env python
import sys

(last_key, sum_val)=(None,0)
for line in sys.stdin:
	(key,val) = line.strip().split('\t')
	if last_key and last_key!=key:
		print '%s\t%s' % (last_key, sum_val)
		(last_key,sum_val)=(key,val)
	else:
		(last_key,sum_val)=(key, int(sum_val)+int(val))
if last_key:
	print '%s\t%s' % (last_key, sum_val)

