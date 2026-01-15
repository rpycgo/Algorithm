import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.tree = [0] * (N * 4)
        self.build(1, 0, N-1)

    def select_min_index(self, idx1, idx2):
        if idx1 == -1:
            return idx2
        if idx2 == -1:
            return idx1

        if self.arr[idx1] < self.arr[idx2]:
            return idx1
        elif self.arr[idx1] > self.arr[idx2]:
            return idx2
        else:
            return min(idx1, idx2)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = start
            return self.tree[node]

        mid = (start + end) // 2
        left_idx = self.build(node*2, start, mid)
        right_idx = self.build(node*2 + 1, mid+1, end)

        self.tree[node] = self.select_min_index(left_idx, right_idx)

        return self.tree[node]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return -1

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_idx = self.query(node*2, start, mid, left, right)
        right_idx = self.query(node*2 + 1, mid+1, end, left, right)

        return self.select_min_index(left_idx, right_idx)

    def update(self, node, start, end, target_idx, new_val):
        if target_idx < start or target_idx > end:
            return self.tree[node]

        if start == end:
            self.arr[target_idx] = new_val
            self.tree[node] = target_idx

            return self.tree[node]

        mid = (start + end) // 2
        left_idx = self.update(node*2, start, mid, target_idx, new_val)
        right_idx = self.update(node*2 + 1, mid+1, end, target_idx, new_val)

        self.tree[node] = self.select_min_index(left_idx, right_idx)

        return self.tree[node]


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())

    segment_tree = SegmentTree(N, A)

    for _ in range(M):
        operator, i, j = map(int, input().split())

        if operator == 1:
            segment_tree.update(1, 0, N-1, i-1, j)
        else:
            idx = segment_tree.query(1, 0, N-1, i-1, j-1)

            print(idx + 1)
