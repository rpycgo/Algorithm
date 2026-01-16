import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N):
        self.N = N

        self.answer = 0

        self.tree = [0] * (4 * N)

    def find_k_th(self, node, start, end, k):
        if start == end:
            return start

        mid = (start + end) // 2

        if self.tree[node*2] >= k:
            return self.find_k_th(node*2, start, mid, k)
        else:
            return self.find_k_th(node*2 + 1, mid+1, end, k-self.tree[node*2])


    def update(self, node, start, end, target_idx, diff):
        if target_idx < start or target_idx > end:
            return self.tree[node]

        if start == end:
            self.tree[node] += diff
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.update(node*2, start, mid, target_idx, diff)
        right_val = self.update(node*2 + 1, mid+1, end, target_idx, diff)

        self.tree[node] = left_val + right_val

        return self.tree[node]


if __name__ == '__main__':
    MAX_VAL = 2_000_000
    segment_tree = SegmentTree(MAX_VAL)

    N = int(input())
    for _ in range(N):
        cmd, X = map(int, input().split())

        if cmd == 1:
            segment_tree.update(1, 1, MAX_VAL, X, 1)
        else:
            kth_val = segment_tree.find_k_th(1, 1, MAX_VAL, X)
            print(kth_val)

            segment_tree.update(1, 1, MAX_VAL, kth_val, -1)
