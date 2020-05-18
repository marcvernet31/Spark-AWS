import nltk
from nltk.tokenize import TweetTokenizer
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local","Nombre")
spark=SparkSession(sc)
tkn=TweetTokenizer()
text_file=spark.read.json('Tweets.json').rdd

#hashtags = text_file.flatMap(lambda x: tkn.tokenize(x["text"])).filter(lambda x: x.startswith('#')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).takeOrdered(5, key=lambda x: x[1])
#hashtags = text_file.flatMap(lambda x: tkn.tokenize(x["text"])).filter(lambda x: x.startswith('#')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).takeOrdered(5, key=lambda x: -x[1])
hashtags = text_file.map(extract_text).flatMap(lambda txt: tkn.tokenize(txt)).filter(lambda word: word.startswith('#')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b).takeOrdered(5, key=lambda x: -x[1])
for x in hashtags:
    print (x)
