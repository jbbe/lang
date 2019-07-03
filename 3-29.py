import nltk
from nltk.corpus import brown
import matplotlib.pyplot as plt

def ari(cat):
    """Accept text as list of words"""
    num_chars = len(brown.raw(categories=cat))
    num_words = len(brown.words(categories=cat))
    num_sents = len(brown.sents(categories=cat))

    avg_word_len = num_chars / num_words
    avg_sent_len = num_words / num_sents

    return avg_word_len * 4.71 + avg_sent_len * 0.5 - 21.43

aris = [(cat, ari(cat)) for cat in brown.categories()]
# plt(aris)
# plt.plot(aris)
# fdist = nltk.FreqDist(aris)
# fdist.tabulate()
# fdist.plot()
# print(aris)