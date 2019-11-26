import nltk, random
from nltk.stem import WordNetLemmatizer
from nltk.corpus import movie_reviews
from nltk.stem import porter, lancaster
documents = [(list(movie_reviews.words(fileid)), category)
                for category in movie_reviews.categories()
                for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]
lemma = WordNetLemmatizer()
lan = lancaster.LancasterStemmer()
port = porter.PorterStemmer()
def document_features_lemmas(document):
    document_words = set([lemma.lemmatize(w) for w in set(document)])
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
def document_features_port(document):
    document_words = set([port.stem(w) for w in set(document)])
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
def document_features_lanc(document):
    document_words = set([lan.stem(w) for w in set(document)])
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
featuresets = [(document_features_lemmas(d), c) for (d,c) in documents]
size = int(0.1*len(featuresets))
train_set, test_set = featuresets[size:], featuresets[:size]
# print(len(featuresets))
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set)) 
# featuresets = [(document_features_lanc(d), c) for (d,c) in documents]
train_set, test_set = featuresets[size:], featuresets[:size]
# print(len(featuresets))
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set)) 
featuresets = [(document_features_port(d), c) for (d,c) in documents]
train_set, test_set = featuresets[size:], featuresets[:size]
# print(len(featuresets))
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set)) 