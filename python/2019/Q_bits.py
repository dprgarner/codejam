"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys
import math


class BaseCaseHandler():
    """
    Boilerplate class.
    """

    def __init__(self):
        self.source = self.get_source()

    def get_source(self):
        try:
            while True:
                yield sys.stdin.readline()
        except EOFError:
            pass

    def read(self):
        return next(self.source).strip()

    def write(self, txt):
        print(str(txt))
        sys.stdout.flush()

    def debug(self, *txt):
        # Uncomment for debugging.
        return
        print(*[str(t) for t in txt], file=sys.stderr)

    def run(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


class CaseComplete(Exception):
    pass


class CaseHandler(BaseCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de
    """

    # These should be enough for B < 16.
    STRINGS = [
        (16, ('0' * 16 + '1' * 16) * (1024 // 32)),
        (8, ('0' * 8 + '1' * 8) * (1024 // 16)),
        (4, ('0' * 4 + '1' * 4) * (1024 // 8)),
        (2, ('0' * 2 + '1' * 2) * (1024 // 4)),
        (1, ('0' * 1 + '1' * 1) * (1024 // 2)),
    ]

    def handle_case(self, _):
        responses = []
        n, b, f = (int(x) for x in self.read().split(' '))
        self.debug('case:', n, b, f)
        for _, s in self.STRINGS:
            self.write(s[:n])
            responses.append(self.read())

        n, responses = self.normalize(n, b, responses)
        soln = self.solve(n, b, responses)
        output = ' '.join(str(x) for x in sorted(soln))
        self.debug('soln: ', output)
        self.write(output)
        verdict = int(self.read())
        assert verdict == 1, verdict

    def normalize(self, n, b, responses):
        # Add working bits to the responses so that all strings are of a
        # length that is a power of two.
        new_n = 2 ** math.ceil(math.log2(n))
        for i, (_, s) in enumerate(self.STRINGS):
            responses[i] += s[n:new_n]
        return new_n, responses

    def count(self, trial):
        zeroes = 0
        ones = 0
        for c in trial:
            if c == '0':
                zeroes += 1
            else:
                ones += 1
        return [zeroes, ones]

    def get_initial_blocks(self, response, n, b):
        count = 0
        previous_blocks = []
        current_bit = '0'
        for c in response:
            if c != current_bit:
                # Flip bit
                current_bit = '1' if current_bit == '0' else '0'
                previous_blocks.append(count)
                count = 0
            count += 1
        previous_blocks.append(count)
        return previous_blocks

    def solve(self, n, b, responses):
        req_res = [
            (block, s[:n], res)
            for (block, s), res in zip(self.STRINGS, responses)
            if block <= n
        ]
        self.debug('req/res pairs:', req_res)

        block_size, request, response = req_res[0]
        previous_blocks = self.get_initial_blocks(response, n, b)

        for block_size, request, response in req_res[1:]:
            self.debug(block_size, request, response)

            next_blocks = []
            str_index = 0
            self.debug('prev blocks', previous_blocks)
            for working in previous_blocks:
                trial_str = response[str_index:str_index + working]
                next_blocks.extend(self.count(trial_str))
                str_index += working
            previous_blocks = next_blocks

        self.debug('final blocks', previous_blocks)
        broken = []
        for (i, res) in enumerate(previous_blocks):
            if res == 0:
                broken.append(i)

        return broken


CaseHandler().run()
