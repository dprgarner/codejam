"""
A script to generate random numbers for this problem:
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1
"""
from random import randrange

u = 16
trials = 10**4

mapping = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
    '7': 'H',
    '8': 'I',
    '9': 'J',
}


def tostr(n):
    return ''.join([
        mapping[c]
        for c in str(n)
    ])


leading = {}
digit_count = {}

for _ in range(trials):
    m = randrange(1, 10**u)
    n = randrange(1, m + 1)
    s = tostr(n)
    # print(s)
    # print('-1 {}'.format(s))
    leading[s[0]] = leading.get(s[0], 0) + 1
    for x in s:
        digit_count[x] = digit_count.get(x, 0) + 1

# for (char, v) in sorted(leading.items(), key=lambda x: -x[1]):
#     print(v, char)

# print('---')
# for (char, v) in sorted(digit_count.items(), key=lambda x: -x[1]):
#     print(v, char)
