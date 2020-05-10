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
        return  # Comment out for debugging
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
        n, responses = self.normalize(n, responses)
        bit_strs = [
            bit_str
            for (block, _), bit_str in zip(self.STRINGS, responses)
            if block <= n
        ]
        soln = self.solve(bit_strs)

        output = ' '.join(str(x) for x in sorted(soln))
        self.debug('soln: ', output)
        self.write(output)
        verdict = int(self.read())
        assert verdict == 1, verdict

    def normalize(self, n, responses):
        """
        Add working bits to the responses so that all strings are of a
        length that is a power of two.
        """
        new_n = 2 ** math.ceil(math.log2(n))
        for i, (_, s) in enumerate(self.STRINGS):
            responses[i] += s[n:new_n]
        return new_n, responses

    def count_bits(self, bit_str):
        zeroes = 0
        ones = 0
        for c in bit_str:
            if c == '0':
                zeroes += 1
            else:
                ones += 1
        return [zeroes, ones]

    def get_initial_blocks(self, bit_str):
        """
        Counts the sizes of the initial alternating groups of 0s and 1s.
        """
        count = 0
        blocks = []
        current_bit = '0'
        for c in bit_str:
            if c != current_bit:
                current_bit = '1' if current_bit == '0' else '0'
                blocks.append(count)
                count = 0
            count += 1
        blocks.append(count)
        return blocks

    def solve(self, bit_strs):
        self.debug('normalized bit strings:', bit_strs)
        blocks = self.get_initial_blocks(bit_strs[0])

        for bit_str in bit_strs[1:]:
            # Blocks are strings of bits of the same digit.
            #
            # On each iteration, the list `blocks` is a list of integers where
            # each integer is how many working machines there are in the
            # block. The size of a block of completely-working machines is
            # always a power of two.
            #
            # On each iteration, break down the previous block in two, and
            # deduce the number of working machines in each half, to generate
            # the next value of the block sizes list.
            self.debug('blocks at current iteration:', blocks)
            next_blocks = []
            bit_str_idx = 0
            for working_bits in blocks:
                bit_substr = bit_str[bit_str_idx:bit_str_idx + working_bits]
                next_blocks.extend(self.count_bits(bit_substr))
                bit_str_idx += working_bits
            blocks = next_blocks

        self.debug('final blocks:', blocks)
        broken_idxs = []
        for (i, res) in enumerate(blocks):
            if res == 0:
                broken_idxs.append(i)

        return broken_idxs


CaseHandler().run()
