import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

        self.tree = [0] * (4 * n)
        self.build(1, 0, n-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return self.tree[node]

        mid = (start + end) // 2
        left_min = self.build(node*2, start, mid)
        right_min = self.build(node*2 + 1, mid+1, end)

        self.tree[node] = min(left_min, right_min)

        return self.tree[node]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return float('inf')

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        left_val = self.query(node*2, start, mid, left, right)
        right_val = self.query(node*2+1, mid+1, end, left, right)

        return min(left_val, right_val)

    def get_min(self, a, b):
        return self.query(1, 0, self.n-1, a-1, b-1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = [int(input()) for _ in range(N)]

    segment_tree = SegmentTree(N, nums)

    for _ in range(M):
        a, b = map(int, input().split())

        print(segment_tree.get_min(a, b))
