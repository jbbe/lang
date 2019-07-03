import os

tiles = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 
         'g' : 2, 'h' :4, 'i': 1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1,
         'p': 3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8,'y':4,'z':10 }

tile_counts = {'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3, 'h': 2,
                'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2,
                'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2, 'x': 1, 'y': 2, 'z': 1}
print(tiles)
longest = 'a'
high_score = 0
with open('/usr/share/dict/words') as words:
    for word in words:
        if len(word) < 4 or '-' in word:
            continue
        score = 0
        print(word)

        for letter in word:
            if letter == '\n':
                continue
            score = score + tiles[letter.lower()]
        if score > high_score:
            for letter in word:
                over = 0
                if letter == '\n':
                    continue
                if word.count(letter) > tile_counts[letter]:
                    over = word.count(letter) - tile_counts[letter]
            if over < 2:
                high_score = score
                longest = word
                print(score, longest)

print(longest, high_score)
        
        