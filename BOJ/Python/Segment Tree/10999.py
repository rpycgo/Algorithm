import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.tree = [0] * (N * 4)
        self.lazy = [0] * (N * 4)

        self.build(1, 0, N-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.build(node*2, start, mid)
        right_val = self.build(node*2 + 1, mid+1, end)

        self.tree[node] = left_val + right_val

        return self.tree[node]

    def query(self, node, start, end, left, right):
        self.update_lazy(node, start, end)

        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.query(node*2, start, mid, left, right)
        right_val = self.query(node*2 + 1, mid+1, end, left, right)

        return left_val + right_val

    def update(self, node, start, end, left, right, diff):
        self.update_lazy(node, start, end)

        if left > end or right < start:
            return self.tree[node]

        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * diff

            if start != end:
                self.lazy[node*2] += diff
                self.lazy[node*2 + 1] += diff

            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.update(node*2, start, mid, left, right, diff)
        right_val = self.update(node*2 + 1, mid+1, end, left, right, diff)

        self.tree[node] = left_val + right_val

        return self.tree[node]

    def update_lazy(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]

            if start != end:
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2 + 1] += self.lazy[node]

            self.lazy[node] = 0


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]

    segment_tree = SegmentTree(N, nums)

    for _ in range(M + K):
        a, b, c, *d = map(int, input().split())

        if a == 1:
            segment_tree.update(1, 0, N-1, b-1, c-1, d[0])
        else:
            result = segment_tree.query(1, 0, N-1, b-1, c-1)

            print(result)
