import nltk, random, re
from nltk.corpus import names
from nltk.classify import apply_features

def assemble_set():
    brown = nltk.corpus.brown.sents() + nltk.corpus.gutenberg.sents()
    appearances = []
    for sent in brown:
        if 'strong' in sent:
            pos = sent.index('strong')
            appearances.append(((sent[:pos] + sent[pos+1:], pos), 'strong'))
        if 'powerful' in sent:
            pos = sent.index('powerful')
            appearances.append(((sent[:pos] + sent[pos+1:], pos), 'powerful'))
    return appearances

labeled_sents = assemble_set()
print(len(labeled_sents))
def inst_features(inst):
        p = inst[1] 
        # print(inst.context, p, len(inst.context))
        if p != 0:
            left = ' '.join(inst[0][p-2:p])
        else:
            left = ''
        if len(inst[0]) < p+3:
            right = ' '.join(inst[0][p+1:p+3])
        else:
            right = ''
        # print(left,right)
        return {
        'left': left, 
        'right': right
        }
size = int(0.2*len(labeled_sents))
train_set = apply_features(inst_features, labeled_sents[:size])
print(train_set)
test_set = apply_features(inst_features, labeled_sents[size:])
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(15))

# tree_classifier = nltk.DecisionTreeClassifier.train(train_set)
# print('tree', nltk.classify.accuracy(tree_classifier, test_set))
# print(tree_classifier.pseudocode(4))

# max_ent_classifier = nltk.MaxentClassifier.train(train_set)
# print('maxenttree', nltk.classify.accuracy(max_ent_classifier, test_set))
# print(max_ent_classifier.show_most_informative_features(10))