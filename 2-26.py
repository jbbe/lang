
from nltk.corpus import wordnet as wn
import numpy as np

# 2-26
# print(np.mean([len(noun.hypernyms()) for noun in wn.all_synsets('n')]))
# (len([noun for noun in wn.all_synsets('n') if noun.hyponyms() == []]))
# union = nltk.corpus.state_union

# 2-27
print('noun: ', np.mean([len(wn.synsets(str(noun.name()).split('.')[0], 'n')) for noun in wn.all_synsets('n')]))

print('verb: ', np.mean([len(wn.synsets(str(noun.name()).split('.')[0], 'n')) for noun in wn.all_synsets('v')]))
    
print('adj: ', np.mean([len(wn.synsets(str(noun.name()).split('.')[0], 'n')) for noun in wn.all_synsets('a')]))
print('adv: ', np.mean([len(wn.synsets(str(noun.name()).split('.')[0], 'n')) for noun in wn.all_synsets('r')]))