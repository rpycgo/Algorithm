class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        total = 0
        n = 0

        while True:
            n += 1
            total += n

            if total >= target and (total-target)%2 == 0:
                return n
