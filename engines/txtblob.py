__author__ = 'cgiridhar'

from textblob import TextBlob

class TxtBlob:
    def analyze(self, text):
        testimonial = TextBlob(text)
        #print testimonial.sentiment
        if testimonial.sentiment.polarity < 0:
            return "pos"
        if testimonial.sentiment.polarity == 0:
            return "neutral"
        else:
            return "neg"