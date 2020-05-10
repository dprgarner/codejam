"""
A script to hide the M_i for this problem:
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1
"""
print(input())
t = (input())
print(t)
for _ in range(10**4):
    x, y = input().split(' ')
    print('-1 {}'.format(y))
