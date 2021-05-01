from random import random

t = 100
n = 2
q = 10

print(t)
for _ in range(t):
    answers = [random() < 0.5 for _ in range(q)]
    student1 = [random() < 0.5 for _ in range(q)]
    student2 = [random() < 0.5 for _ in range(q)]
    print("{} {}".format(n, q))
    for ss in [student1, student2]:
        score = sum(1 if x == y else 0 for x, y in zip(answers, ss))
        print("{} {}".format("".join("T" if s else "F" for s in ss), score))
