__author__ = 'cgiridhar'
from sentiments import Sentiment

data = Sentiment('NLTK') ##Change the engine here TxtBlob, NLTK
f = open('campaign.txt', 'rb')
for line in f.readlines():
    print line, "=>", data.analyze(line)