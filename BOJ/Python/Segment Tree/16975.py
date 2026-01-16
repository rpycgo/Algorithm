import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.tree = [0] * (4 * N)

        self.build(1, 0, N-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.build(node*2, start, mid)
        self.build(node*2 + 1, mid+1, end)

    def query(self, node, start, end, idx):
        if start == end:
            return self.tree[node]

        mid = (start + end) // 2
        if idx <= mid:
            return self.tree[node] + self.query(node*2, start, mid, idx)
        else:
            return self.tree[node] + self.query(node*2 + 1, mid+1, end, idx)

    def update(self, node, start, end, left, right, diff):
        if right < start or end < left:
            return

        if left <= start and end <= right:
            self.tree[node] += diff
            return self.tree[node]

        mid = (start + end) // 2
        self.update(node*2, start, mid, left, right, diff)
        self.update(node*2 + 1, mid+1, end, left, right, diff)


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    segment_tree = SegmentTree(N, nums)

    M = int(input())
    for _ in range(M):
        row = tuple(map(int, input().split()))

        if row[0] == 1:
            _, i, j, k = row
            segment_tree.update(1, 0, N-1, i-1, j-1, k)
        else:
            x = row[1]
            result = segment_tree.query(1, 0, N-1, x-1)

            print(result)
