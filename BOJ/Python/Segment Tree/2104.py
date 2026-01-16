import sys


sys.setrecursionlimit(200000)
input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = [float('inf')] + arr

        self.h = N.bit_length()
        self.size = 1 << self.h

        self.sum_tree = [0] * (self.size * 2)
        self.min_idx_tree = [0] * (self.size * 2)

        self._build()

    def _get_min_idx(self, idx1, idx2):
        if idx1 == 0:
            return idx2
        if idx2 == 0:
            return idx1

        return idx1 if self.arr[idx1] < self.arr[idx2] else idx2

    def _build(self):
        for i, val in enumerate(self.arr):
            self.sum_tree[self.size + i] = val
            self.min_idx_tree[self.size + i] = i

        for i in range(self.size-1, 0, -1):
            self.sum_tree[i] = self.sum_tree[i*2] + self.sum_tree[i*2 + 1]
            self.min_idx_tree[i] = self._get_min_idx(self.min_idx_tree[i*2], self.min_idx_tree[i*2 + 1])

    def _query_sum(self, left, right):
        left += self.size
        right += self.size

        total = 0
        while left <= right:
            if left%2 == 1:
                total += self.sum_tree[left]
                left += 1

            if right%2 == 0:
                total += self.sum_tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def _query_min_idx(self, left, right):
        left += self.size
        right += self.size

        min_idx = 0
        while left <= right:
            if left%2 == 1:
                min_idx = self._get_min_idx(min_idx, self.min_idx_tree[left])
                left += 1

            if right%2 == 0:
                min_idx = self._get_min_idx(min_idx, self.min_idx_tree[right])
                right -= 1

            left //= 2
            right //= 2

        return min_idx

    def query(self, left, right):
        if left > right:
            return 0

        if left == right:
            return self.arr[left] * self.arr[left]

        idx = self._query_min_idx(left, right)
        curr_sum = self._query_sum(left, right)

        curr_score = curr_sum * self.arr[idx]
        left_score = self.query(left, idx-1)
        right_score = self.query(idx+1, right)
        max_score = max(curr_score, left_score, right_score)

        return max_score


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    segment_tree = SegmentTree(N, nums)

    result = segment_tree.query(1, N)
    print(result)
