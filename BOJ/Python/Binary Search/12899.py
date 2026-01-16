import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N):
        self.size = 1
        while self.size < N:
            self.size *= 2

        self.tree = [0] * (self.size * 2)

    def find_k_th(self, k):
        idx = 1
        while idx < self.size:
            left_idx = idx * 2

            if self.tree[left_idx] >= k:
                idx = left_idx
            else:
                k -= self.tree[left_idx]
                idx = left_idx + 1

        return idx - self.size + 1


    def update(self, target_idx, diff):
        idx = self.size + target_idx - 1

        while idx > 0:
            self.tree[idx] += diff

            idx //= 2


if __name__ == '__main__':
    MAX_VAL = 2_000_000
    segment_tree = SegmentTree(MAX_VAL)

    N = int(input())
    for _ in range(N):
        cmd, X = map(int, input().split())

        if cmd == 1:
            segment_tree.update(X, 1)
        else:
            kth_val = segment_tree.find_k_th(X)
            print(kth_val)

            segment_tree.update(kth_val, -1)
