import re
s = 'colorless'
s = s[:4] + 'u' + s[4:]
print(s)

strings = ['dishes', 'running', 'nationality', 'undo', 'preheat']

print(strings[0][:-2])
print(strings[1][:-4])
print(strings[2][:-5])
print(strings[3][:-2])
print(strings[4][:-4])

# print(strings[4][-8])
s = "this is a wonderful fucking series of exercises"
"""
    [a-zA-Z]+   return all words with only standard latin letters
    [A-Z][a-z]* return all words started with only standard latin letters follwoed by anything
    p[aeiou]{,2}t all words that have a p and a t with up to two vowels between
    \d+(\.\d+)? a number followed by a period followed by a number
    ([^aeiou][aeiou][^aeiou])* contains a consonant followed by a vowel followed by a consonant
    \w+|[^\w\s]+ Tokenize a text into a sequence of alphabetic and
    non-alphabetic characters because its either \w word characters
        or in the second case not words or whitespace

"""

#9 a
raw = """This will be a story of terror. It will be a story of police, a tale of darkness 
and of terror. But it will not seem so. It will not seem so because I am the one who tells it. 
I am the one who tells it and for that it will not seem so. But at its heart, this is the 
story of an appalling crime.
"""


def find_determiners(string):
    return re.findall(r'(an|a|the)', string)

def find_arith_exp(string):
    return re.findall(r'\d+\*\d+\+\d+', string)

arit = "ok  2*3+8 shlkj 45*54+5"
print(find_determiners(s))
print(find_determiners(raw))

print(find_arith_exp(arit))

