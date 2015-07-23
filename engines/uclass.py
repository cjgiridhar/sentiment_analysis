__author__ = 'cgiridhar'

import requests, json

class uClassify:

    def analyze(self, text):
        r = requests.get(
            'https://uclassify.com/browse/uclassify/sentiment/ClassifyText'
            '?readkey=3hqvKRgROB9u&output=json&version=1.01&text='
            + text
        )
        positive = (json.loads(r.text))['cls1']['positive']
        negative = (json.loads(r.text))['cls1']['negative']

        if positive > negative:
            return "pos"
        if positive == negative:
            return "neutral"
        else:
            return "neg"