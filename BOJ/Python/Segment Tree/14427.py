import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = [float('inf')] + arr

        self.h = N.bit_length()
        self.size = 1 << self.h

        self.tree = [0] * (2 * self.size)

        self._build()

    def _get_min_index(self, idx1, idx2):
        if idx1 == 0:
            return idx2
        if idx2 == 0:
            return idx1

        if self.arr[idx1] < self.arr[idx2]:
            return idx1
        elif self.arr[idx1] > self.arr[idx2]:
            return idx2
        else:
            return min(idx1, idx2)

    def _build(self):
        for i in range(1, self.N+1):
            self.tree[self.size + i] = i

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self._get_min_index(self.tree[i*2], self.tree[i*2 + 1])

    def query(self):
        return self.tree[1]

    def update(self, target_idx, new_val):
        self.arr[target_idx] = new_val

        idx = self.size + target_idx
        while idx > 1:
            idx //= 2
            self.tree[idx] = self._get_min_index(self.tree[idx*2], self.tree[idx*2 + 1])


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    segment_tree = SegmentTree(N, nums)

    M = int(input())
    for _ in range(M):
        row = list(map(int, input().split()))

        if row[0] == 2:
            result = segment_tree.query()
            print(result)
        else:
            _, i, v = row

            segment_tree.update(i, v)
