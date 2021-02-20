
def solve_case(k):
    if k == 0:
        return None
    digits = set(str(s) for s in range(10))
    current = k

    attempts = 0
    while attempts < 1000:
        for char in str(current):
            # print(char)
            if char in digits:
                digits.remove(char)
        # print(digits)
        if not digits:
            break
        current += k
        attempts += 1

    if attempts == 100:
        raise Exception('ran out of attempts')
    return current


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        k = int(input())
        soln = solve_case(k)
        if soln:
            print(
                "Case #{}: {}".format(i, soln),
                flush=True,
            )
        else:
            print("Case #{}: INSOMNIA".format(i), flush=True)


if __name__ == "__main__":
    run()
