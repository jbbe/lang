import nltk
from nltk.corpus import ppattach
from pickle import dump
ppattach.attachments('training')
inst = ppattach.attachments('training')[2]
print(inst)
print((inst.noun1, inst.prep, inst.noun2))

def noun_features(inst):

    return {'noun1': inst.noun1,
            'noun2': inst.noun2,
            'pos1': nltk.pos_tag(inst.noun1),
            'pos2': nltk.pos_tag(inst.noun2),
            }


nattach = [({'noun1': inst.noun1, 'noun2': inst.noun2}, inst.prep)for inst in ppattach.attachments('training') if inst.attachment == 'N']
size = int(0.1*len(nattach))
train_set, test_set = nattach[size:], nattach[:size]


# classifier = nltk.MaxentClassifier.train(train_set)
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))

output = open('prep_classifier.pkl', 'wb')
dump(classifier, output, -1)
output.close()
