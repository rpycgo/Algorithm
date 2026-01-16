import sys
from bisect import bisect_right


input = sys.stdin.readline


class MergeSortTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.h = N.bit_length()
        self.size = 1 << self.h

        self.tree = [[] for _ in range(2 * self.size)]

        self._build()

    def _build(self):
        for i, val in enumerate(self.arr):
            self.tree[self.size + (i + 1)] = [val]

        for i in range(self.size-1, 0, -1):
            self.tree[i] = sorted(self.tree[i*2] + self.tree[i*2 + 1])

    def query(self, left, right, k):
        left += self.size
        right += self.size

        total = 0
        while left <= right:
            if left%2 == 1:
                total += len(self.tree[left]) - bisect_right(self.tree[left], k)
                left += 1

            if right%2 == 0:
                total += len(self.tree[right]) - bisect_right(self.tree[right], k)
                right -= 1

            left //= 2
            right //= 2

        return total


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    segment_tree = MergeSortTree(N, nums)

    M = int(input())
    for _ in range(M):
        i, j, k = map(int, input().split())

        result = segment_tree.query(i, j, k)
        print(result)
