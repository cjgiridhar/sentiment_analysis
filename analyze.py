__author__ = 'cgiridhar'

from sentiments import Sentiment
engines = ['TxtBlob', 'NLTK', 'Indico', 'uClassify']

##Change the engine here

f = open('text.txt', 'rb')
for line in f.readlines():
    for engine in engines:
        data = Sentiment(engine)
        print line.strip(), "=>", engine, "=>", data.analyze(line)
