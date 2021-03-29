import sys
from random import random, randint
import math

t = 100

print(t)
print(86)
players = 100
questions = 10000

correct = 0
incorrect = 0


def debug(*str):
    print(*str, file=sys.stderr, flush=True)


for _ in range(t):
    ss = [random() * 6 - 3 for _ in range(players)]
    qs = [random() * 6 - 3 for _ in range(questions)]

    cheat = 5  # randint(0, players)
    cheater_score = 0
    for idx, s in enumerate(ss):
        for q in qs:
            if idx == (cheat - 1) and randint(0, 1) == 0:
                bit = "1"
                cheater_score += 1
            elif random() < (1 / (1 + math.exp(q - s))):
                bit = "1"
                if idx == (cheat - 1):
                    cheater_score += 1
            else:
                bit = "0"
            sys.stdout.write(bit)
        sys.stdout.write("\n")

    sys.stdout.flush()

    # debug("First ten q difficulties:")
    # for i in range(10):
    #     debug(qs[i])

    # debug("First six skills:")
    # for i in range(6):
    #     debug(ss[i])

    # debug("Cheater score:", cheater_score)

    answer = int(input().split(": ")[1])
    if answer == cheat:
        correct += 1
    else:
        incorrect += 1

    # debug("dishonest skill", ss[cheat - 1])

    debug(
        "Accuracy: {:.2f}%\t ({} / {})\n".format(
            100 * correct / (correct + incorrect),
            correct,
            correct + incorrect,
        ),
    )
