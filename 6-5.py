import nltk, random
from nltk.corpus import names
from nltk.classify import apply_features


def base_line_features(w):
    return {'last_letter': w[-1]}

def gender_features(w):
    return {
    # 'last_letter': w[-1:].lower(), 
    'length': len(w),
    'first_two_letter': w[:3],
    # 'suffix2': w[-2:],
    'suffix3': w[-4:],
    }

labeled_names =[]
with open('names.txt', 'r') as f:
    for line in f:
        name, label = line.strip('\n').split(', ')
        labeled_names.append((name, label))
# gender_features = base_line_features

train_set = apply_features(gender_features, labeled_names[6900:])
test_set = apply_features(gender_features, labeled_names[6900:7400])
devtest_names = labeled_names[6900:7400]
devtest_set = apply_features(gender_features, labeled_names[7400:])

bayes_classifier = nltk.NaiveBayesClassifier.train(train_set)
print('bayes', nltk.classify.accuracy(bayes_classifier, devtest_set))
print('bayes', nltk.classify.accuracy(bayes_classifier, test_set))
print(bayes_classifier.show_most_informative_features(10))

tree_classifier = nltk.DecisionTreeClassifier.train(train_set)
print('tree', nltk.classify.accuracy(tree_classifier, devtest_set))
print('tree', nltk.classify.accuracy(tree_classifier, test_set))
print(tree_classifier.pseudocode(4))

max_ent_classifier = nltk.MaxentClassifier.train(train_set)
print('maxenttree', nltk.classify.accuracy(max_ent_classifier, devtest_set))
print('maxenttree', nltk.classify.accuracy(max_ent_classifier, test_set))
print(max_ent_classifier.show_most_informative_features(10))