import nltk
from nltk.corpus import brown

def occurs_n_times(n):
    fdist = nltk.FreqDist([w.lower() for w in brown.words(categories=brown.categories())])
    return [w for w in fdist if fdist[w] >= n]

print(occurs_n_times(3))