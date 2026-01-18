import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N):
        self.N = N

        self.tree = [0] * (4 * N)
        self.lazy = [0] * (4 * N)

    def _apply_lazy(self, node, start, end):
        if self.lazy[node]%2 == 1:
            self.tree[node] = (end - start + 1) - self.tree[node]

            if start != end:
                self.lazy[node*2] += 1
                self.lazy[node*2 + 1] += 1

            self.lazy[node] = 0

    def query(self, node, start, end, left, right):
        self._apply_lazy(node, start, end)

        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.query(node*2, start, mid, left, right)
        right_val = self.query(node*2 + 1, mid+1, end, left, right)

        return left_val + right_val

    def update(self, node, start, end, left, right):
        self._apply_lazy(node, start, end)

        if right < start or end < left:
            return

        if left <= start and end <= right:
            self.lazy[node] += 1
            self._apply_lazy(node, start, end)

            return

        mid = (start + end) // 2
        self.update(node*2, start, mid, left, right)   
        self.update(node*2 + 1, mid+1, end, left, right)

        self.tree[node] = self.tree[node*2] + self.tree[node*2 + 1]


if __name__ == '__main__':
    N, M = map(int, input().split())

    segment_tree = SegmentTree(N)

    for _ in range(M):
        O, S, T = map(int, input().split())

        if O == 0:
            segment_tree.update(1, 0, N-1, S-1, T-1)
        else:
            result = segment_tree.query(1, 0, N-1, S-1, T-1)
            print(result)
