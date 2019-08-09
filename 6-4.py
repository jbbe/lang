import nltk, random

from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
                for category in movie_reviews.categories()
                for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
print(len(featuresets))
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set)) 
print(classifier.show_most_informative_features(30))

# the most important features were overwhelmingly negative 
# Many were names which makes sense to the degre that certain reviewers might be 
# more prone to negative reviews than others
# many of the rest seem to be negative adjectives which is interesting to me
# either the training set was too small or having martians just makes movies bad
# the inclusion of welles name was interesting to me as it was tilted neg