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

# labeled_names =[]
with open('names.txt', 'r') as f:
    for line in f:
        name, label = line.strip('\n').split(', ')
        labeled_names.append((name, label))
# gender_features = base_line_features
train_set = apply_features(gender_features, labeled_names[6900:])
test_set = apply_features(gender_features, labeled_names[6900:7400])
devtest_names = labeled_names[6900:7400]
devtest_set = apply_features(gender_features, labeled_names[7400:])
classifier = nltk.NaiveBayesClassifier.train(train_set)



errors = []
for (name, tag) in devtest_names:
    # print(name)
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )
        print(tag, guess, name)

print(nltk.classify.accuracy(classifier, devtest_set))
# with open('names.txt', 'w+') as f:
#     for name in labeled_names:
#         f.write(''.join([name[0], ', ', name[1], '\n']))

# print(nltk.classify.accuracy(classifier, test_set))
