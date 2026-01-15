import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.tree = [0] * (N * 4)

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
        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.query(node*2, start, mid, left, right)
        right_val = self.query(node*2 + 1, mid+1, end, left, right)

        return left_val + right_val

    def update(self, node, start, end, target_idx, new_val):
        if target_idx < start or target_idx > end:
            return self.tree[node]

        if start == end:
            self.tree[node] = new_val
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.update(node*2, start, mid, target_idx, new_val)
        right_val = self.update(node*2 + 1, mid+1, end, target_idx, new_val)

        self.tree[node] = left_val + right_val

        return self.tree[node]


if __name__ == '__main__':
    N, Q = map(int, input().split())
    nums = list(map(int, input().split()))

    segment_tree = SegmentTree(N, nums)

    for _ in range(Q):
        x, y, a, b = map(int, input().split())

        if x > y:
            x, y = y, x

        result = segment_tree.query(1, 0, N-1, x-1, y-1)
        print(result)

        segment_tree.update(1, 0, N-1, a-1, b)
