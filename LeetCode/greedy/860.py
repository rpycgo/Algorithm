class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n_5 = 0
        n_10 = 0

        for bill in bills:
            if bill == 5:
                n_5 += 1
            elif bill == 10:
                if n_5 >= 1:
                    n_5 -= 1
                    n_10 += 1
                else:
                    return False
            elif bill == 20:
                if n_10 >= 1 and n_5 >= 1:
                    n_5 -= 1
                    n_10 -= 1
                elif n_5 >= 3:
                    n_5 -= 3
                else:
                    return False

        return True
