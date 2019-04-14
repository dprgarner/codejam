from codejam import CodeJamParser


# 19:53 - 20:48 (with some distraction)

class Run(CodeJamParser):
    """
    2014, Qualification round, D
    https://code.google.com/codejam/contest/2974486/dashboard#s=p0
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            blocks = int(next(self.source))
            naomi = [
                float(c) for c in next(self.source).split(' ') 
            ]
            ken = [
                float(c) for c in next(self.source).split(' ') 
            ]
            yield naomi, ken

    def handle_case(self, naomi, ken):
        blocks = len(naomi)

        # "Deceitful War" score
        naomi_copy = [n for n in naomi]
        ken_copy = [n for n in ken]
        deceit_score = 0
        while naomi_copy:
            min_k = min(ken_copy)
            if min_k > max(naomi_copy):
                # Ken wins all remaining points
                break
            best_n = min([n for n in naomi_copy if n > min_k])
            ken_copy.remove(min_k)
            naomi_copy.remove(best_n)
            deceit_score += 1

        # "War" score
        naomi_copy = [n for n in naomi]
        ken_copy = [n for n in ken]
        score = 0
        for _ in range(blocks):
            max_n = max(naomi_copy)
            naomi_copy.remove(max_n)
            if max_n > max(ken_copy):
                ken_copy.remove(min(ken_copy))
                score += 1
            else:
                ken_copy.remove(max(ken_copy))
        return '{} {}'.format(deceit_score, score)

if __name__ == '__main__':
    Run()
