import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, size):
        self.n = 1
        while self.n < size:
            self.n *= 2

        self.tree = [0] * (self.n * 2)

    def query(self, left, right):
        left += self.n
        right += self.n

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

    def update(self, target_idx, val):
        idx = self.n + target_idx
        self.tree[idx] = val

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[idx*2] + self.tree[idx*2 + 1]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        orders = list(map(int, input().split()))

        total_size = n + m
        segment_tree = SegmentTree(total_size)

        pos = [0] * (n + 1)
        for i in range(1, n + 1):
            pos[i] = m + i - 1
            segment_tree.update(pos[i], 1)

        answer = []

        top = m - 1
        for order in orders:
            curr_pos = pos[order]

            cnt = segment_tree.query(0, curr_pos-1)
            answer.append(cnt)

            segment_tree.update(curr_pos, 0)

            pos[order] = top
            segment_tree.update(pos[order], 1)

            top -= 1

        answer = ' '.join(map(str, answer))
        print(answer)
