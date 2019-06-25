import nltk
from nltk.corpus import stopwords
# for cat in brown.categories():
#         print(cat, ' '* (15-len(cat)), lexical_diversity(brown.words(categories=cat)))

def most_common_bigrams(text):
        bigrams = nltk.bigrams(text)
        bigrams_no_stops = [bigram for bigram  in bigrams if bigram[0] not in stopwords.words('english') and bigram[1] not in stopwords.words('english')]
        cfd = nltk.ConditionalFreqDist(bigrams)
        cfd.tabulate()
        print(sorted(cfd.items(), key=lambda k_v: k_v[1][2], reverse=True))

def most_common_non_stop_words(text):
    fdist = nltk.FreqDist([w for w in text if w not in stopwords.words('english')])
    return fdist.most_common(n=50)
    

