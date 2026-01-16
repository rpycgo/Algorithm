import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = [float('inf')] + arr

        self.h = N.bit_length()
        self.size = 1 << self.h

        self.tree = [0] * (self.size * 2)

        self._build()

    def _convert(self, val):
        return 1 if val%2 == 0 else 0

    def _build(self):
        for i, val in enumerate(self.arr):
            self.tree[self.size + i] = self._convert(val)

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]

    def query(self, left, right):
        left += self.size
        right += self.size

        total = 0
        while left <= right:
            if left%2 == 1:
                total += self.tree[left]
                left += 1

            if right%2 == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def update(self, target_idx, new_val):
        idx = self.size + target_idx
        self.tree[idx] = self._convert(new_val)

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[idx*2] + self.tree[idx*2 + 1]


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    segment_tree = SegmentTree(N, nums)

    M = int(input())
    for _ in range(M):
        cmd, x, y = map(int, input().split())

        if cmd == 1:
            segment_tree.update(x, y)
        else:
            result = segment_tree.query(x, y)

            if cmd == 3:
                result = (y - x + 1) - result

            print(result)
