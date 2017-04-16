import math
from codejam import CodeJamParser


def optimise_attacks(H_k, A_d, B):
    if B == 0:
        return (math.ceil(H_k / A_d), 0)
    # Find best buff/attack strategy.
    # s = a + b, minimised at a_0 subject to knight being defeated
    a_0 = math.sqrt(H_k / B)
    s = math.ceil(a_0 + (H_k - a_0 * A_d) / (a_0 * B))
    while (True):
        # For an integer s above the cts min,
        # find bounds of allowable region in a.
        try:
            discriminant = math.sqrt((A_d + s*B)**2 - 4 * B * H_k)
        except:
            import pdb
            pdb.set_trace()
        a_min = math.ceil((A_d + s * B - discriminant) / (2 * B))
        a_max = math.floor((A_d + s * B - discriminant) / (2 * B))
        if a_min <= a_max:
            break
        s += 1
    return a_min, s - a_min


def check_hp(start_hp, current_attack, D):
    hps = []
    hp = start_hp
    for i in range(10):
        current_attack = max(0, current_attack - D)
        hp = hp - current_attack
        if hp <= 0:
            break
        hps.append(hp)
    return hps


def debuffs_before_need_to_cure(start_hp, current_attack, D):
    discriminant = (D - 2 * current_attack) ** 2 - 8 * D * start_hp
    if discriminant < 0:
        return None  # Never need to cure.
    debuffs_cts = (
        (2 * current_attack - D - math.sqrt(discriminant)) / (2 * D)
    )
    debuffs = math.floor(debuffs_cts)
    if debuffs == debuffs_cts:  # Exactly zero HP
        debuffs -= 1
    # check = check_hp(start_hp, current_attack, D)
    # if len(check) != debuffs:
    #     print(current_attack, D, check, debuffs)
    return debuffs


def turns_to_apply_d_debuffs_with_cures(initial_H_d, initial_A_k, D, d):
    """
    I gave up on this while implementing this function.
    This is unfinished.
    """
    # debuffs_applied = 0
    # debuffs_remaining = d
    # cures = 0
    # H_d, A_k = initial_H_d, initial_A_k
    # while True:
    #     debuffs = debuffs_before_need_to_cure(H_d, A_k, D)
    #     if debuffs < debuffs_remaining:
    #     if debuffs == None:
    #         # Calc how many debuffs were applied before attack fell to zero.
    #         debuffs_applied += math.ceil(A / D)
    #         break
    #     debuffs_applied += debuffs
    #     if debuffs_applied > d:
    #         break
    #     debuffs_remaining -= debuffs
    #     cures += 1
    #     A_k = A_k - D * debuffs
    #     H_d = initial_H_d - A_k  # The knight gets an attack in the cure turn.
    # return (debuffs_applied + cures)


def optimise_defence(H_d, A_k, D, offensive_turns):
    # No more need to debuff.
    # Lower the knight's attach as much as you need to, to minimise the need
    # to cure.
    return 0, 0


class Dragon(CodeJamParser):
    """
    2017, Qualification round, A, practice
    https://code.google.com/codejam/contest/5304486/dashboard#s=p2&a=1
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            H_d, A_d, H_k, A_k, B, D = [
                int(x) for x in next(self.source).split(' ')
            ]
            yield H_d, A_d, H_k, A_k, B, D

    def handle_case(self, H_d, A_d, H_k, A_k, B, D):
        # Should first buff this many times, then attack this many times.
        # min # of turns to win is attacks + buffs.
        attacks, buffs = optimise_attacks(H_k, A_d, B)
        offensive_turns = attacks + buffs
        cures, debuffs = optimise_defence(H_d, A_k, D, offensive_turns)
        defensive_turns = cures + debuffs
        return str(offensive_turns + defensive_turns)



if __name__ == '__main__':
    # Dragon()
    # for i in range(30):
    #     for j in range(30):
    #         debuffs_before_need_to_cure(30, i+1, j+1)