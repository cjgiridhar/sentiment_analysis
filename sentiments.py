__author__ = 'cgiridhar'

from engines.nltoolkit import NLTK
from engines.txtblob import TxtBlob
from engines.uclass import uClassify
from engines.indico import Indico

class Sentiment:
    def __init__(self, engine):
        self.engine = engine

    def analyze(self, text):
        return eval(self.engine)().analyze(text)

