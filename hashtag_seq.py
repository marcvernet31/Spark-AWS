import nltk
from nltk.tokenize import TweetTokenizer
from collections import Counter
import json
import sys

filename = sys.argv[1]
tkn=TweetTokenizer()
with open(filename,'r') as f:
    d=f.readlines()
    d = str(d)
    texto = d
    tokens = tkn.tokenize(texto)
    hashtags = [t for t in tokens if t.startswith('#')]
    print contador.most_common(5)

#    contador = Counter()
#    for linea in f:
#        tweet = json.loads(linea)
#        if "text" in tweet:
#            if tweet["truncated"] == True:
#                texto = tweet["extended_tweet"]["full_text"]
#            else:
#                texto=tweet["text"]
#        tokens = tkn.tokenize(texto)
#        hashtags = [t for t in tokens if t.startswith('#')]
#        contador.update(hashtags)
#    print contador.most_common(5)
