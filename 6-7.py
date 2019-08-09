import nltk


posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialog_act_features(posts, i, history):
    features = {}
    for word in nltk.word_tokenize(posts[i].text):
        features['contains({})'.format(word.lower())] = True
    if i == 0:
        features["prev-post"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-post"] = history[i-1]
        features["prev-tag"] = history[i-1].get('class')
    return features

class ConsecutiveDialogActTagger(nltk.TaggerI):
    def __init__(self, train_posts):
        train_set = []
        for tagged_post in train_posts:
            untagged_posts = nltk.tag.untag(tagged_post)
            history = []
            for i, (post, tag) in enumerate(tagged_posts):
                featureset = pos_features(untagged_post, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, post):
        history = []
        for i, word in enumerate(post):
            featureset = dialog_act_features(post, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(post, history)

# featuresets = [(dialogue_act_features(post.text), post.get('class'))
#                for post in posts]
size = int(len(posts) * 0.1)
train_set, test_set = posts[size:], posts[:size]
tagger = ConsecutiveDialogActTagger(train_set)
print(tagger.evaluate(test_set))