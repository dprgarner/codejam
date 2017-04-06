from os import sys


def get_lines_from_stdin():
    try:
        while True:
            yield input()
    except EOFError:
        pass


def get_lines_from_file(input_file):
    with open(input_file, 'r') as in_:
        while True:
            line = in_.readline().replace('\n', '')
            if not line:
                break
            yield line


class CodeJamParser(object):
    def __init__(self):
        self.source = get_lines_from_stdin()
        if len(sys.argv) > 1:
            self.source = get_lines_from_file(sys.argv[1])

        if len(sys.argv) > 2:
            with open(sys.argv[2], 'w') as out_:
                self.dest = out_
                self.write_cases()
        else:
            self.dest = sys.stdout
            self.write_cases()

    def write_cases(self):
        for i, case in enumerate(self.get_cases()):
            result = self.handle_case(*case)
            self.dest.write('Case #{}: {}\n'.format(i + 1, result))

    def get_cases(self):
        raise NotImplementedError(
            'Override this method to iterate over '
            'self.source and yield cases as tuples.'
        )

    def handle_case(self, *args):
        raise NotImplementedError(
            'Override this method to take the same number of arguments as'
            'were yielded from get_cases, and output the resulting string.'
        )