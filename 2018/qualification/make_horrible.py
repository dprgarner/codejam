"""
A script for generating horrible inputs for 2018, Qualification round, B
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
"""
from random import random

print(1)
for _ in range(1):
    print(10**5)
    for i in range(10**5):
        print('{}'.format(int(random() * 10**9)), end='')
        if i == 10**5 - 1:
            print('\n', end='')
        else:
            print(' ', end='')
