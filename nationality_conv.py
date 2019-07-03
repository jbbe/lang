import nltk

NATION_DICT = {}

def make_dict():

    with open('nationality_list.txt') as f:
        for line in f:
            line.strip()
            if len(line.split()) < 2:
                continue
            NATION_DICT[line.split()[1].lower()] = line.split()[0]
            for i in range(2, len(line.split())):
                NATION_DICT[line.split()[i].lower()] = line.split()[0]         

def conv_nat(name):
    if name.lower() not in NATION_DICT:
        return ''
    return NATION_DICT[name.lower()]
if __name__ == '__main__':
    make_dict()
    print(NATION_DICT)