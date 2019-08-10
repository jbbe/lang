import nltk, random
from nltk.corpus import names
from nltk.classify import apply_features
import math

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p,2) for p in probs)

def gender_features(w):
    return {'last_letter': w[-1:].lower(), 
    'length': len(w), 
    'first_two_letter': w[:2].lower(),
    'suffix2': w[-2:],
    'suffix3': w[-3:]}

def gender_features2(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')])


random.shuffle(labeled_names)
# Just last letter gave acc of 0.752
# featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set = apply_features(gender_features, labeled_names[500:])
test_set = apply_features(gender_features, labeled_names[:500])
classifier = nltk.NaiveBayesClassifier.train(train_set)

# print(classifier.classify(gender_features('Neo')))
# print(classifier.classify(gender_features('Trinity')))
# print(classifier.show_most_informative_features(5))

train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]
# def gender_features(word):
    # return {'suffix1': word[-1:], 'suffix2': word[-2:]}

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, devtest_set))
# errors = []
# for (name, tag) in devtest_names:
#     guess = classifier.classify(gender_features(name))
#     if guess != tag:
#         errors.append( (tag, guess, name) )
        # print(tag, guess, name)


## 1.3

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

#
# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# print(nltk.classify.accuracy(classifier, test_set)) 
# print(classifier.show_most_informative_features(5))

from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]

# print(common_suffixes)

def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
    return features

# tagged_words = brown.tagged_words(categories='news')
# featuresets = [(pos_features(n), g) for (n,g) in tagged_words]

# size = int(len(featuresets) * 0.1)
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.DecisionTreeClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.pseudocode(depth=7))

def pos_features(sentence, i):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features

# pos_features(brown.sents()[0], 8)
# tagged_sents = brown.tagged_sents(categories='news')
# featuresets = []

# for tagged_sent in tagged_sents:
#     untagged_sent = nltk.tag.untag(tagged_sent)
#     for i, (word, tag) in enumerate(tagged_sent):
#         featuresets.append( (pos_features(untagged_sent, i), tag) )

# size = int(len(featuresets) * 0.1)
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# print(nltk.classify.accuracy(classifier, test_set))


def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

# tagged_sents = brown.tagged_sents(categories='news')
# size = int(len(tagged_sents) * 0.1)
# train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]
# tagger = ConsecutivePosTagger(train_sents)
# print(tagger.evaluate(test_sents))


## Sentence Classification

# sents = nltk.corpus.treebank_raw.sents()
# tokens = []
# boundaries = set()
# offset = 0
# for sent in sents:
#     tokens.extend(sent)
#     offset += len(sent)
#     boundaries.add(offset-1)

def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i+1][0].isupper(),
            'prev-word': tokens[i-1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i-1]) == 1}
# featuresets = [(punct_features(tokens, i), (i in boundaries))
#                for i in range(1, len(tokens)-1)
#                if tokens[i] in '.?!']

# size = int(len(featuresets) * 0.1)
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(35))

  	

def segment_sentences(words):
    start = 0
    sents = []
    for i, word in enumerate(words):
        if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
            sents.append(words[start:i+1])
            start = i+1
    if start < len(words):
        sents.append(words[start:])
    return sents


posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features


  	

# featuresets = [(dialogue_act_features(post.text), post.get('class'))
#                for post in posts]
# size = int(len(featuresets) * 0.1)
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(35))

def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features

rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])
extractor = nltk.RTEFeatureExtractor(rtepair)
print(extractor.text_words)
print(extractor.hyp_words)
print(extractor.overlap('word'))
print(extractor.overlap('ne'))
