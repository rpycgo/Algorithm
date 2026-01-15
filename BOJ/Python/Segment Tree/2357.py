import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.min_tree = [0] * (4 * N)
        self.max_tree = [0] * (4 * N)

        self.build_min(1, 0, N-1)
        self.build_max(1, 0, N-1)

    def build_min(self, node, start, end):
        if start == end:
            self.min_tree[node] = self.arr[start]
            return self.min_tree[node]

        mid = (start + end) // 2
        left_min = self.build_min(node*2, start, mid)
        right_min = self.build_min(node*2 + 1, mid+1, end)

        self.min_tree[node] = min(left_min, right_min)

        return self.min_tree[node]

    def build_max(self, node, start, end):
        if start == end:
            self.max_tree[node] = self.arr[start]
            return self.max_tree[node]

        mid = (start + end) // 2
        left_max = self.build_max(node*2, start, mid)
        right_max = self.build_max(node*2 + 1, mid+1, end)

        self.max_tree[node] = max(left_max, right_max)

        return self.max_tree[node]

    def query(self, node, start, end, left, right, target='min'):
        if target == 'min':
            if left > end or right < start:
                return float('inf')

            if left <= start and end <= right:
                return self.min_tree[node]

            mid = (start + end) // 2
            left_val = self.query(node*2, start, mid, left, right)
            right_val = self.query(node*2 + 1, mid+1, end, left, right)

            return min(left_val, right_val)
        else:
            if left > end or right < start:
                return float('-inf')

            if left <= start and end <= right:
                return self.max_tree[node]

            mid = (start + end) // 2
            left_val = self.query(node*2, start, mid, left, right, target='max')
            right_val = self.query(node*2 + 1, mid+1, end, left, right, target='max')

            return max(left_val, right_val)

    def run(self, a, b):
        min_val = self.query(1, 0, self.N-1, a, b, target='min')
        max_val = self.query(1, 0, self.N-1, a, b, target='max')

        return (min_val, max_val)


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = [int(input()) for _ in range(N)]

    segment_tree = SegmentTree(N, nums)

    for _ in range(M):
        a, b = map(int, input().split())

        min_val, max_val = segment_tree.run(a-1, b-1)

        print(min_val, max_val)
