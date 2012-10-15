import sys
import json
from stemming.lovins import stem

# read in the sentiment words
fh = open('sentiment_wordlist.txt','r')
sentiment_wordscores = dict()
pos_words = fh.readline().split(',')
neg_words = fh.readline().split(',')

for w in pos_words:
	sentiment_wordscores[stem(w)] = 1
for w in neg_words:
	sentiment_wordscores[stem(w)] = -1
	
# read in tweets
tweetfile = sys.argv[1]
fh = open(tweetfile,'r')

sentiment = 0

for line in fh:
	try:
		tweet = json.loads(line)
	except:
		break
		
	if 'text' in tweet:
		try:
			text = tweet['text']
			words = text.split()
			for w in words:
				sentiment += sentiment_wordscores.get(stem(w),0)
		except:
			pass
			
print 'Sentiment score:',sentiment
