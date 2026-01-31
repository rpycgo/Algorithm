import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.h = (N-1).bit_length()
        self.size = 1 << self.h

        self.tree = [0] * (2*self.size)
        self.lazy = [0] * (2*self.size)

        self._build()

    def _build(self):
        for i, val in enumerate(self.arr):
            self.tree[i+self.size] = val

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[2*i] ^ self.tree[2*i + 1]

    def query(self, node, start, end, left, right):
        self._apply_lazy(node, start, end)

        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self.query(2*node, start, mid, left, right) ^ \
               self.query(2*node + 1, mid+1, end, left, right)

    def _apply_lazy(self, node, left, right):
        if self.lazy[node] != 0:
            if (right-left+1)%2 == 1:
                self.tree[node] ^= self.lazy[node]

            if left != right:
                self.lazy[2*node] ^= self.lazy[node]
                self.lazy[2*node + 1] ^= self.lazy[node]

            self.lazy[node] = 0

    def update(self, node, start, end, left, right, k):
        self._apply_lazy(node, start, end)

        if right < start or end < left:
            return

        if left <= start and end <= right:
            self.lazy[node] ^= k
            self._apply_lazy(node, start, end)
            return

        mid = (start+end) // 2
        self.update(2*node, start, mid, left, right, k)
        self.update(2*node + 1, mid+1, end, left, right, k)

        self.tree[node] = self.tree[2*node] ^ self.tree[2*node + 1]


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    segment_tree = SegmentTree(N, A)

    M = int(input())
    for _ in range(M):
        cmd, *query = tuple(map(int, input().split()))

        if cmd == 1:
            i, j, k = query
            segment_tree.update(1, 0, segment_tree.size-1, i, j, k)
        elif cmd == 2:
            i, j = query
            print(segment_tree.query(1, 0, segment_tree.size-1, i, j))


if __name__ == '__main__':
    main()
