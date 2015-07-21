__author__ = 'cgiridhar'

import requests,json

class NLTK:

    def analyze(self, text):
        r = requests.post(
                'http://text-processing.com/api/sentiment/',
                data="text=" + text
        )
        #print r.status_code, r.text
        value = (json.loads(r.text))['label']
        return value