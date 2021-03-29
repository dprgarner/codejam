"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
Post-contest solution.
>90% accuracy?
"""
import sys
from math import exp, log


player_count = 100
question_count = 10000


def solve_case(players):
    question_difficulties = []
    for j in range(question_count):
        question_score = 0
        for i in range(player_count):
            if players[i][j] == "1":
                question_score += 1
        # Maths! This comes from the expectation value of the total correct
        # answers to the question, averaging over the distribution of player
        # skills (assuming all honest), and then inverting.
        t = 6 * question_score / player_count
        q = log((exp(3) - exp(t - 3)) / (exp(t) - 1))
        question_difficulties.append(q)

    sorted_difficulties = sorted(question_difficulties)
    hard_threshold = 2.5
    easy_threshold = -hard_threshold
    hard_qs = set(j for j, q in enumerate(question_difficulties) if q > hard_threshold)
    easy_qs = set(j for j, q in enumerate(question_difficulties) if q < easy_threshold)

    max_err = 0
    candidate = 0
    for i in range(player_count):
        player_score = 0
        for j in range(question_count):
            if players[i][j] == "1":
                player_score += 1

        # More Maths! This comes from the expectation value of the player's score,
        # averaging over the distribution of question difficulties, and then
        # inverting.
        r = 6 * player_score / (question_count)
        s = log((exp(3 - r) - exp(3)) / (1 - exp(6 - r)))
        if s > 3.25:
            return i

        err_i = 0
        for set_ in (easy_qs, hard_qs):
            expected_score = sum(
                1 / (1 + exp(question_difficulties[j] - s)) for j in set_
            )
            actual_score = sum(int(players[i][j]) for j in set_)
            err_i += abs(expected_score - actual_score)

        if err_i > max_err:
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
        print("Case #{}: {}".format(i, soln + 1), flush=True)


if __name__ == "__main__":
    run()
