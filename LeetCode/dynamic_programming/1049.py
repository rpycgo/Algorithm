class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        bits = 1
        for stone in stones:
            bits |= bits << stone

        total = sum(stones)
        target = total // 2

        for j in range(target, -1, -1):
            if (bits >> j) & 1:
                return total - 2*j
