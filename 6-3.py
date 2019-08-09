import nltk
from nltk.corpus import senseval

from nltk.classify import apply_features


def classify_instances(set_name):
    def inst_features(inst):
        p = inst.position
        # print(inst.context, p, len(inst.context))
        if p == 0:
            left = ' '.join(w for (w,t) in inst.context[p-2:p])
            left_pos = ' '.join(t for (w,t) in inst.context[p-2:p])
        else:
            left = ''
            left_pos = ''
        word = ' '.join(w for (w,t) in inst.context[p:p+1])
        # print(inst.context[p+1:p+3])
        if len(inst.context) > p+3:
            if len(inst.context[p+1]) == 2:
                right_pos = inst.context[p+1][1]
            elif len(inst.context[p+2]) == 2:
                right_pos = inst.context[p+2][1]
            elif len(inst.context[p+3]) == 2:
                right_pos = inst.context[p+2][1]
            else:
                right_pos = ''
            right = ' '.join(w[0] for w in inst.context[p+1:p+3] if len(w) == 2)
            # print(right, right_pos)

        else:
            right_pos = ''
            right = ''
        senses = ' '.join(inst.senses)
        return {
        # 'last_letter': word[-1:].lower(), 
        'left': left, 
        'word': word,
        'right': right,
        'left_pos': left_pos,
        'right_pos': right_pos
        }
    instances = senseval.instances(set_name)
    labeled_instances = [(inst, inst.senses[-1]) for inst in instances]
    size = int(len(labeled_instances) * 0.1)

    train_set, test_set = labeled_instances[size:], labeled_instances[:size]
    # print(train_set[0])
    train_set = apply_features(inst_features, labeled_instances[800:])
    test_set = apply_features(inst_features, labeled_instances[:200])
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    errors = []
    for (inst, tag) in labeled_instances[300:]:
        guess = classifier.classify(inst_features(inst))
        if guess != tag:
            errors.append( (tag, guess, inst) )
        print(tag, guess, inst.context[inst.position-2:inst.position+2])
    print(classifier.show_most_informative_features(10))
    print(nltk.classify.accuracy(classifier, test_set))
# for inst in senseval.instances('line.pos'):
#     p = inst.position
#     left = ' '.join(w for (w,t) in inst.context[p-2:p])
#     word = ' '.join(w for (w,t) in inst.context[p:p+1])
#     right = ' '.join(w for (w,t) in inst.context[p+1:p+3])
#     senses = ' '.join(inst.senses)
#     print(p, '%20s |%10s | %-15s -> %s' % (left, word, right, senses))

# for fileid in senseval.fileids():
#     print(fileid)
#     classify_instances(fileid)

classify_instances('line.pos')