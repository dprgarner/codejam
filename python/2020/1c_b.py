"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1
"""


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        _ = int(input())
        leading = {}
        available_digits = set()
        for _ in range(10**4):
            _, s = input().split(' ')
            leading[s[0]] = leading.get(s[0], 0) + 1
            for c in s:
                available_digits.add(c)

        digit = 1
        digits = {}
        for (char, v) in sorted(leading.items(), key=lambda x: -x[1]):
            digits[digit] = char
            digit += 1
        # print(digits)
        last = (available_digits - (set(digits.values())))
        assert len(last) == 1
        digits[0] = last.pop()
        # print(digits)
        soln = ''.join([digits[i] for i in range(10)])
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()
