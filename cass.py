#!/usr/bin/env python
from cassandra.cluster import Cluster
import re
import os

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

pos_percentage_before = round(((count2 / float(count2 + count)) * 100), 2)
neg_percentage_after = round(((count / float(count2 + count)) * 100), 2)

pos_percentage_after = round(((count4 / float(count4 + count3)) * 100), 2)
neg_percentage_before = round(((count3 / float(count4 + count3)) * 100), 2)

f1 = open('copy_index.html','r')
f2 = open('index.html','w')

f2.truncate()


fullspan = "<span class='text-muted' id='data'></span>"
beginspan = "<span class='text-muted' id='data'>"
#fullspan_pos = "<span class='text-muted' id='pos'></span>"
#beginspan_pos = "<span class='text-muted' id='pos'>"
#fullspan_neg = "<span class='text-muted' id='neg'></span>"
#beginspan_neg = "<span class='text-muted' id='neg'>"
endspan = "</span>"

before_text = "<br>Percentage of Positive Tweets Before: " + str(pos_percentage_before) + "% <br> Percentage of Negative Tweets Before: " + str(neg_percentage_before) + "%"

after_text = "<br>Percentage of Positive Tweets After: " + str(pos_percentage_after) + "% <br> Percentage of Negative Tweets After: " + str(neg_percentage_after) + "%"

numb_pos = "<br>Total Positive Tweets Before: " + str(count2) + "<br> Total Negative Tweets Before: " + str(count)

numb_neg = "<br>Total Positive Tweets After: " + str(count3) + "<br> Total Negative Tweets After: " + str(count4)

for line in f1:
	f2.write(line.replace(fullspan, beginspan + numb_pos + numb_neg + before_text + after_text + endspan))

f1.close()
f2.close()	

os.system("elinks index.html")

