import nltk
from nltk.corpus import wordnet as wn

class NovelIndex:
    def __init__(self, text):
        self._text = text

    def _novel_uses(self, word):
        """
        measures of similarity:
                    path_similarity
                    lch_similarity
                    wup_similarity -- how similar two word senses are
        """
        
