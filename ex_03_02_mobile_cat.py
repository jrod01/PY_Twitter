import sys
import json
import csv

tweetfile = sys.argv[1]

# load the mobility designations
mobility = {}
MOBILE = 'TRUE'
NOT_MOBILE = 'FALSE'
MIXED = 'MIXED'
fh = open('user_agents.csv','r')
fiter = iter(fh)
fiter.next(); fiter.next()
reader = csv.reader(fiter,delimiter=',',quotechar='"')
for data in reader:
	mobility[data[0]] = data[2]

# count the number of mobile vs. non-mobile tweets
num_mobile = 0
num_mixed = 0
num_nonmobile = 0
num_unknown = 0

fh = open(tweetfile,'r')
for line in fh:
	try:
		tweet = json.loads(line)
	except:
		break
	if 'text' not in tweet:
		continue
	source = tweet['source'].encode('ascii','ignore')
	
	if source not in mobility:
		num_unknown += 1
	elif mobility[source] == MOBILE:
		num_mobile += 1
	elif mobility[source] == NOT_MOBILE:
		num_nonmobile += 1
	elif mobility[source] == MIXED:
		num_mixed += 1
	else:
		print 'Unknown mobility designation for %s' % source
		quit()
		
print 'Mobile: ',num_mobile
print 'Non-mobile:', num_nonmobile
print 'Mixed:', num_mixed
print 'Unknown:',num_unknown
