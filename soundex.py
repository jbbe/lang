import nltk, re

def run_soundex(name):
    """
    1. retain first letter of name and map aeiouyhw
    2. replace consonants with digits
    3. Drop second of back to back pairs of same coded letters
        or same coded letters seperated by h or w are coded as 1
        but those seperated by a vowel are coded seperatey
    4. If elength is less than
    """
    mapping = [name[0]]
    for letter in name[1:]:
        mapping.append(map_letter(letter))
    print(mapping)
    second_map = [name[0]]
    for i in range(2,len(mapping)):
        if mapping[i] != mapping[i-1] and mapping[i] != 0:
            second_map.append(mapping[i])
        if mapping[i - 1] == 0:
            if i > 2:
                if mapping[i-2] == mapping[i]:
                    if name[i-1] in 'wh':
                        second_map.append(mapping[i])
    while(len(second_map) < 3):
        second_map.append(0)
    return second_map
            



def map_letter(letter):
    zero = 'aeiouyhw'
    one = 'bfpv'
    two = 'cgjkqsxz'
    three = 'dt'
    four = 'l'
    five = 'mn'
    six = 'r'
    if letter in zero:
        return 0
    if letter in one:
        return 1
    if letter in two:
        return 2
    if letter in three:
        return 3
    if letter in four:
        return 4
    if letter in five:
        return 5
    if letter in six:
        return 6
    return -1


print(run_soundex("johannes"))
print(run_soundex("Robert"))
print(run_soundex("Rupert"))
print(run_soundex("Tymczak"))
print(run_soundex("Honeyman"))
print(run_soundex("Phister"))