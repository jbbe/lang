import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
           (genre, word)
           for genre in ['romance', 'news', 'adventure', 'humor'] 
           for word in brown.words(categories=genre))

print('string')

cfd.plot(samples=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])