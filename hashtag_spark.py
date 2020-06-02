import nltk
from nltk.tokenize import TweetTokenizer
from pyspark import SparkContext
from pyspark.sql import SparkSession
import sys

tkn = TweetTokenizer()

sc = SparkContext("spark://ip-172-31-77-235.ec2.internal:7077", "Nombre")
spark = SparkSession(sc)

filename = sys.argv[1]
text_file = spark.read.json(filename).rdd

def  extract_text(tweet):
    try:
        if tweet["truncated"] == True:
            return tweet["extended_tweet"]["full_text"].encode('ascii','ignore')
        else:
            return tweet["text"].encode('ascii','ignore')
    except:
        return []

hashtags = text_file.flatMap(lambda x: tkn.tokenize(extract_text(x))).filter(lambda x:x.startswith('#')).map(lambda word:(word,1)).reduceByKey(lambda a, b: a+b).takeOrdered(5, key=lambda x: -x[1])

for x in hashtags:
    print(x)
