class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []

        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)

    def pickIndex(self) -> int:
        r = randint(1, self.prefix[-1])

        idx = bisect_left(self.prefix, r)

        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()