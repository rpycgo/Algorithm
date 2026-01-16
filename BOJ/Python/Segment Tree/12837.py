import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N):
        self.h = N.bit_length()
        self.size = 1 << self.h

        self.tree = [0] * (self.size * 2)

    def query(self, left, right):
        left += self.size
        right += self.size

        total = 0
        while left <= right:
            if left%2 == 1:
                total += self.tree[left]
                left += 1

            if right%2 == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def update(self, target_idx, new_val):
        idx = self.size + target_idx
        self.tree[idx] += new_val

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[idx*2] + self.tree[idx*2 + 1]


if __name__ == '__main__':
    N, Q = map(int, input().split())

    segment_tree = SegmentTree(N)

    for _ in range(Q):
        cmd, x, y = map(int, input().split())

        if cmd == 1:
            segment_tree.update(x, y)
        else:
            result = segment_tree.query(x, y)
            print(result)
