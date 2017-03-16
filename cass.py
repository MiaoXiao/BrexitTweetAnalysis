#!/usr/bin/env python
from cassandra.cluster import Cluster

cluster = Cluster(port=9043)
session = cluster.connect("projecttest")

sentNegative = session.execute("COUNT * FROM tweets_sentimenttest WHERE score<0")
sentPositive = session.execute("COUNT * FROM tweets_sentimenttest WHERE score>0")
