words = ['attribution', 'confabulation', 'elocution',
            'sequoia', 'tenacious', 'unidirectional']

vsequence = sorted(set([''.join([char for char in word if char in 'aeiou']) for word in words]))

print(vsequence)

