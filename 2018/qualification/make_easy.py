"""
A script for generating easy inputs for 2018, Qualification round, B
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
"""
from random import random

c = 100
print(c)

for _ in range(c):
    n = 3 + int(random() * 20)
    print(n)
    numbers = [int(random() * 100) for _ in range(n)]
    odds = numbers[1::2]
    evens = numbers[::2]
    odds.sort()
    evens.sort()

    if len(evens) > len(odds):
        for i in range(n // 2):
            print('{} {} '.format(evens[i], odds[i]), end='')
        print('{}'.format(evens[n // 2 - 1]))
    else:
        for i in range(n // 2):
            print('{} {}'.format(evens[i], odds[i]), end='')
            if i == n // 2 - 1:
                print('\n', end='')
            else:
                print(' ', end='')
