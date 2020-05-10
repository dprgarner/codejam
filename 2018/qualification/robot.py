from os import sys


class CodeJamParser(object):
    """
    Copy/paste this file, extend this class overriding the methods get_cases and handle_case, and call CodeJam.

    Use this class by initialising at the top level and piping to stdin/stdout.
    """

    @staticmethod
    def get_lines_from_stdin():
        try:
            while True:
                yield input()
        except EOFError:
            pass

    def __init__(self):
        self.source = get_lines_from_stdin()
        self.dest = sys.stdout
        self.write_cases()

    def write_cases(self):
        for i, case in enumerate(self.get_cases()):
            result = self.handle_case(*case)
            self.dest.write('Case #{}: {}\n'.format(i + 1, result))


IMPOSSIBLE = 'IMPOSSIBLE'


def get_damage(attacks):
    damage = 0
    power = 1
    for c in attacks:
        if c == 'C':
            power *= 2
        else:
            damage += power
    return damage


class Codejam(CodeJamParser):
    """
    2018, Qualification round, A
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            shield, attacks = case_line.split(' ')
            yield int(shield), attacks

    def handle_case(self, shield, attacks):
        # print(shield, attacks, ':', get_damage(attacks))
        if sum([1 for c in attacks if c == 'S']) > shield:
            return IMPOSSIBLE

        # Always possible. Start from the end, move the charges to the end. Best
        # move is always to swap the last CS to SC.
        turns = 0
        while True:
            if get_damage(attacks) <= shield:
                return turns
            cs = len(attacks) - attacks[::-1].index('SC') - 2
            # print('last cs at: ', cs)
            attacks = attacks[:cs] + 'SC' + attacks[cs + 2:]
            turns += 1


Codejam()
