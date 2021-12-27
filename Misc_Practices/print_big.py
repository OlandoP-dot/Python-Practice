# Print a 5x5 representation of a given alphabet letter.
# Only did until letter F, the rest is essentially the same, just different patterns.
# Doing a bit of dictionary mapping and function usage practice.

import sys

def print_big(letter):
    patterns = {1:'  *  ', 2:' * * ', 3:'*****', 4:'*   *', 5:'***  ', 6:'*  * ', 7:'*     ', 8:'**** ', 9:' ****'}
    alphabet = {'A':[1,2,3,4,4], 'B':[5,6,5,6,5], 'C':[9,7,7,7,9], 'D':[8,4,4,4,8], 'E':[8,7,5,7,8], 'F':[3,7,5,7,7]}

    for x in alphabet[letter.upper()]:
        print(patterns[x])


if len(sys.argv)<2:
    letter = input("Enter letter from a-f: ")
    print_big(letter)
else:
    print_big(sys.argv[1])
