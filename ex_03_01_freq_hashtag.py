import sys
import json

tweetfile = sys.argv[1]
k = int(sys.argv[2])

fh = open(tweetfile,'r')
hashtag_abundance = {}

for line in fh:
	try:
		tweet = json.loads(line)
	except:
		break

	if 'text' not in tweet:
		continue
	text = tweet['text']
		
	hts = tweet['entities']['hashtags']
	for hinfo in hts:
		h = hinfo['text']
		hashtag_abundance[h] = 1 + hashtag_abundance.get(h,0)
		
	# 
	# # extract hashtags
	# i = text.find('#',0)
	# while i > 0:
	# 	j = text.find(' ',i)
	# 	
	# 	hashtag = text[i:j]
	# 	hashtag_abundance[hashtag] = 1 + hashtag_abundance.get(hashtag,0)
	# 	
	# 	i = text.find('#',j)

hts = hashtag_abundance.items()
hts.sort(cmp=lambda x,y: -cmp(x[1],y[1]))

for ht,a in hts[:k]:
	print ht,a