import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, size):
        self.size = size

        self.tree = [0] * (4 * size)

    def query(self, node, start, end, left, right):
        if right < start or end < left:
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
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        orders = list(map(int, input().split()))

        total_size = n + m
        segment_tree = SegmentTree(total_size)

        pos = [0] * (n + 1)
        for i in range(1, n + 1):
            pos[i] = n + i - 1
            segment_tree.update(1, 0, total_size-1, pos[i], 1)

        answer = []

        top = m - 1
        for order in orders:
            curr_pos = pos[order]

            cnt = segment_tree.query(1, 0, total_size-1, 0, curr_pos-1)
            answer.append(cnt)

            segment_tree.update(1, 0, total_size-1, curr_pos, 0)

            pos[order] = top
            segment_tree.update(1, 0, total_size-1, pos[order], 1)
            top -= 1

        answer = ' '.join(map(str, answer))
        print(answer)
