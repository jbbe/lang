import nltk
from itertools import chain
from nltk.metrics import accuracy

def dialog_act_features(post, i, history):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    if i == 0:
        features["prev1-tag"] = "<START>"
    elif i == 1:
        features["prev1-tag"] = history[i-1]
        features["prev2-tag"] = "<START>"
    else:
        features["prev1-tag"] = history[i-1]
        features["prev2-tag"] = history[i-2]
    return features

class ConsecutiveDialogActTagger(nltk.TaggerI):
    def __init__(self, train_posts):
        train_set = []
        untagged_posts = nltk.tag.untag(train_posts)
        history = []
        for i, (post, tag) in enumerate(train_posts):
            featureset = dialog_act_features(untagged_posts[i], i, history)
            train_set.append( (featureset, tag) )
            history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, posts):
        history = []
        post_tags = []
        for i, post in enumerate(posts):
            
            featureset = dialog_act_features(post, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
            # print(i, post, tag)
            post_tags.append((post, tag))
        return post_tags 

    def tag_sents(self, sentences):
        """
        Apply ``self.tag()`` to each element of *sentences*.  I.e.:

            return [self.tag(sent) for sent in sentences]
        """
        return [self.tag(sent) for sent in sentences]

    def evaluate(self, gold):
        """
        Score the accuracy of the tagger against the gold standard.
        Strip the tags from the gold standard text, retag it using
        the tagger, then compute the accuracy score.

        :type gold: list(list(tuple(str, str)))
        :param gold: The list of tagged sentences to score the tagger on.
        :rtype: float
        """

        tagged_posts = self.tag(nltk.tag.untag(gold))
        # gold_tokens = list(chain(*gold))
        gold_tags = [t for (w,t) in gold]
        test_tags = [t for (w,t) in tagged_posts]
        # print(len(gold_tags), len(test_tags))
        # print(test_tags)
        # test_tokens = list(chain(*tagged_posts))
        # print(len(tagged_posts))
        # , len(gold_tokens), len(test_tokens))
        return accuracy(gold_tags, test_tags)    

# posts = nltk.corpus.nuntagged_postsps_chat.xml_posts()[:10000]
posts = nltk.corpus.nps_chat.xml_posts()[:10000]
featuresets = [((post.text), post.get('class'))
               for post in posts]
size = int(len(posts) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
tagger = ConsecutiveDialogActTagger(train_set)
print(tagger.evaluate(test_set))