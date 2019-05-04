"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys
import math


class BaseInteractiveCaseHandler():
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

    def run(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


class ImpossibleException(Exception):
    pass


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134c90
    """

    def handle_case(self, i):
        a = int(self.read())
        strategies = []
        for _ in range(a):
            strategies.append(self.read())
        try:
            soln = self.solve(strategies)
        except ImpossibleException:
            soln = 'IMPOSSIBLE'
        self.write('Case #{}: {}'.format(i, soln))

    def solve(self, strategies):
        a = len(strategies)
        k = int(math.log2(a + 1))
        # strategies.sort()
        next_strategies = set()

        # Next strategies of all robots.
        my_moves = []
        move_number = 0
        while move_number < 500:
            # print('strategies left:', len(strategies))
            next_strategies = set()
            for strategy in strategies:
                next_strategies.add(strategy[move_number % len(strategy)])
                # print('robot move: ', strategy[move_number % len(strategy)])
            if len(next_strategies) == 3:
                raise ImpossibleException
            if len(next_strategies) == 2:
                # print('2 strats, not sure yet')
                # No optimal strategy, pick the one that beats one and ties the other
                if next_strategies == set(['P', 'R']):
                    my_moves.append('P')
                elif next_strategies == set(['R', 'S']):
                    my_moves.append('R')
                elif next_strategies == set(['S', 'P']):
                    my_moves.append('S')

                # Remove the beaten robots
                for i in range(len(strategies) - 1, -1, -1):
                    strategy = strategies[i]
                    if strategy[move_number % len(strategy)] != my_moves[-1]:
                        strategies.pop(i)

            if len(next_strategies) == 1:
                # print('1 strats, solved')
                # We have a strategy!
                if next_strategies == set('P'):
                    my_moves.append('S')
                elif next_strategies == set('R'):
                    my_moves.append('P')
                elif next_strategies == set('S'):
                    my_moves.append('R')
                return ''.join(my_moves)
            move_number += 1

        # Too long
        raise ImpossibleException


CaseHandler().run()
