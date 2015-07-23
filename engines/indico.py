__author__ = 'cgiridhar'
import indicoio

class Indico:

    def analyze(self, text):
        indicoio.config.api_key = '051003141c2626e19f0acf007730258f'
        value = indicoio.sentiment(text)
        if value == 0.5:
            return "neutral"
        if value > 0.5:
            return "pos"
        else:
            return "neg"