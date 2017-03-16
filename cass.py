#!/usr/bin/env python
from cassandra.cluster import Cluster

cluster = Cluster(port=9043)
session = cluster.connect("projecttest")
count = 0
count2 = 0
count3 = 0
count4 = 0

sentNegative23 = session.execute("SELECT * FROM projecttest.tweets_sentimenttest where score < 0 allow filtering")
sentPositive23 = session.execute("SELECT * FROM projecttest.tweets_sentimenttest where score > 0 allow filtering")

for sent in sentNegative23:
	count +=1
for sent in sentPositive23:
	count2 +=1
print "June 23rd negative and positive :"
print count
print count2
sentNegative24 = session.execute("SELECT * FROM projecttest.tweets_sentimenttest24 where score < 0 allow filtering")
sentPositive24 = session.execute("SELECT * FROM projecttest.tweets_sentimenttest24 where score > 0 allow filtering")

for sent in sentNegative24:
	count3 +=1
for sent in sentPositive24:
	count4 +=1
print "JUne 24th negative and positive :"
print count3
print count4

