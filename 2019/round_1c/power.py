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
        cases, checks = (int(x) for x in self.read().split(' '))
        for i in range(1, cases + 1):
            try:
                self.handle_case(i)
            except WrongAnswerException:
                self.debug('Wrong answer')
                return

    def handle_case(self, i):
        raise NotImplementedError


class CaseHandler(BaseCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134e91
    """

    def get_char_dict(self):
        return {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
        }

    def find_by_count(self, dict_, n):
        for char, value in dict_.items():
            if value == n:
                return char
        raise Exception('Cannot find char')

    def handle_case(self, _):
        self.debug()
        first_char_counts = self.get_char_dict()
        known_chars = []
        for i in range(119):
            self.write(5 * i + 1)
            char = self.read()
            known_chars.append(char)
            first_char_counts[char] += 1

        first_char = self.find_by_count(first_char_counts, 23)
        self.debug('First char counts:', first_char_counts)
        self.debug('First char:', first_char)
        to_check_next = [
            i for i, char in enumerate(known_chars) if char == first_char
        ]
        self.debug(to_check_next)
        assert len(to_check_next) == 23

        second_char_counts = self.get_char_dict()
        for i in to_check_next:
            self.write(5 * i + 2)
            char = self.read()
            known_chars[i] = known_chars[i] + char
            second_char_counts[char] += 1
        second_char = self.find_by_count(second_char_counts, 5)

        self.debug('Second char counts:', second_char_counts)
        self.debug('Second char:', second_char)
        to_check_next = [
            i
            for i, str_ in enumerate(known_chars)
            if len(str_) == 2 and str_[1] == second_char
        ]
        self.debug(to_check_next)
        assert len(to_check_next) == 5

        third_char_counts = self.get_char_dict()
        for i in to_check_next:
            self.write(5 * i + 3)
            char = self.read()
            known_chars[i] = known_chars[i] + char
            third_char_counts[char] += 1
        third_char = self.find_by_count(third_char_counts, 1)
        self.debug('Third char counts:', third_char_counts)
        self.debug('Third char:', third_char)
        to_check_next = [
            i
            for i, str_ in enumerate(known_chars)
            if len(str_) == 3 and str_[2] == third_char
        ]
        assert len(to_check_next) == 1

        i = to_check_next[0]
        self.write(5 * i + 4)
        # Whatever this character is, this char comes in the fifth place,
        # and the missing char comes in fourth place
        fifth_char = self.read()
        fourth_char = set(['A', 'B', 'C', 'D', 'E']).difference(
            set(known_chars[i] + fifth_char)
        ).pop()
        guess = known_chars[i] + fourth_char + fifth_char
        self.debug(guess)
        self.write(guess)

        assert self.read() == 'Y'


CaseHandler().run()
