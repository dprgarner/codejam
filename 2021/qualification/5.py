"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155#analysis
Didn't work. :(
"""
import sys
from math import exp, log


def debug(*str):
    print(*str, file=sys.stderr, flush=True)


player_count = 100
question_count = 10000


def solve_case(players):
    player_scores = []
    for i in range(player_count):
        player_score = 0
        for j in range(question_count):
            if players[i][j] == "1":
                player_score += 1
        player_scores.append(player_score)

    # Maths!
    player_skills_honest = []
    for i, player_score in enumerate(player_scores):
        r = 6 * player_score / (question_count)
        s1 = (exp(3 - r) - exp(3)) / (1 - exp(6 - r))
        s1 = log(s1)
        player_skills_honest.append(s1)

    question_difficulties = []

    for j in range(question_count):
        question_score = 0

        for i in range(player_count):
            if players[i][j] == "1":
                question_score += 1
        q_low = -4
        q_high = 4
        while abs(q_low - q_high) > 0.01:
            q = (q_low + q_high) / 2
            score_trial = sum(
                [1 / (1 + exp(q - s)) for i, s in enumerate(player_skills_honest)]
            )
            if score_trial > question_score:
                # The guessed difficulty is too low
                q_low = q
            else:
                q_high = q

        question_difficulties.append(q)

    sorted_difficulties = sorted(question_difficulties)
    threshold = 100
    hard_threshold = sorted_difficulties[-threshold]
    easy_threshold = sorted_difficulties[threshold]
    hard_qs = set(j for j, q in enumerate(question_difficulties) if q > hard_threshold)
    easy_qs = set(j for j, q in enumerate(question_difficulties) if q < easy_threshold)

    debug(easy_qs)
    debug(hard_qs)
    threshold_qs = hard_qs.union(easy_qs)

    max_err = -1
    candidate = -1
    for i, s in enumerate(player_skills_honest):
        err_i = 0
        q = question_difficulties[j]
        for set_ in (easy_qs, hard_qs):
            expected_score = sum(
                1 / (1 + exp(question_difficulties[j] - s)) for j in set_
            )
            actual_score = sum(int(players[i][j]) for j in set_)
            err_i += abs(expected_score - actual_score)

        # debug(i, "err:", err_i)
        if err_i > max_err:
            debug("new candidate:", i, err_i)
            max_err = err_i
            candidate = i

    return candidate


def run():
    cases = int(input())
    player_count = 100
    _p = int(input())

    for i in range(1, cases + 1):
        players = []
        for _ in range(player_count):
            players.append(input())
        soln = solve_case(players)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
