"""
Demonstrate loading JSON content returned by Twitter API.
"""

import json

fh = open('sample_tweet.json','r')
tweet = json.load(fh)

#print tweet
max_len = max([len(k) for k in tweet])

for k,v in tweet.items():
	print '%s%s' % ((k+':').ljust(max_len+2),str(v))