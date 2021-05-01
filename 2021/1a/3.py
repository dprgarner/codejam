"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/0000000000754750
Gave up.
"""


def solve_case(q, students):
    n = len(students)
    assert n == 2
    diffs = []
    for i in range(q):
        diffs.append(False if students[0][0][i] == students[1][0][i] else True)

    a = students[0][1]
    b = students[1][1]
    s = sum(1 for d in diffs if d == True)
    print("s", s)
    print("q-s", q - s)
    print("lower bounds", 0, a + s - q, b + s - q)
    print("upper bounds", a, b, s)

    min_x = max(0, a + s - q, b + s - q)
    max_x = min(a, b, s)
    print("".join("T" if s else "F" for s in diffs))
    print("vals to check:", min_x, max_x)
    assert min_x <= max_x

    # print(students)
    return ""


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, q = (int(x) for x in input().split(" "))
        students = []
        for _ in range(n):
            answers, score = (x for x in input().split(" "))
            score = int(score)
            answers = list(answers)
            students.append((answers, score))
        soln = solve_case(q, students)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
