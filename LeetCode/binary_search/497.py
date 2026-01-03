class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []

        total = 0
        for x1, y1, x2, y2 in rects:
            x = x2 - x1 + 1
            y = y2 - y1 + 1
            area = x * y

            total += area

            self.prefix.append(total)

    def pick(self) -> List[int]:
        r = randint(1, self.prefix[-1])

        idx = bisect_left(self.prefix, r)
        x1, y1, x2, y2 = self.rects[idx]

        x = randint(x1, x2)
        y = randint(y1, y2)

        return [x, y]




# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()