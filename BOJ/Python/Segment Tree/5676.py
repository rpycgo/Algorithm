import sys


input = sys.stdin.read


class SegmentTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.h = N.bit_length()
        self.size = 1 << self.h

        self.tree = [1] * (2 * self.size)
        self._build()

    def _categorize(self, val):
        if val > 0:
            return 1
        if val < 0:
            return -1

        return 0

    def convert_int_to_symbol(self, val):
        if val == 1:
            return '+'
        if val == -1:
            return '-'

        return '0'

    def _build(self):
        for i, val in enumerate(self.arr):
            self.tree[self.size + (i+1)] = self._categorize(val)

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[i*2] * self.tree[i*2 + 1]

    def query(self, left, right):
        left += self.size
        right += self.size

        total = 1
        while left <= right:
            if left%2 == 1:
                total *= self.tree[left]
                left += 1

            if right%2 == 0:
                total *= self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def update(self, target_idx, new_val):
        idx = self.size + target_idx
        self.tree[idx] = self._categorize(new_val)

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[idx*2] * self.tree[idx*2 + 1]


if __name__ == '__main__':
    data = input().split()
    ptr = 0

    while ptr < len(data):
        N = int(data[ptr])
        K = int(data[ptr+1])
        ptr += 2

        X = tuple(map(int, data[ptr:ptr+N]))
        ptr += N

        segment_tree = SegmentTree(N, X)

        answer = []
        for _ in range(K):
            cmd = data[ptr]
            x = int(data[ptr+1])
            y = int(data[ptr+2])

            ptr += 3

            if cmd == 'C':
                segment_tree.update(x, y)
            elif cmd == 'P':
                result = segment_tree.query(x, y)
                result = segment_tree.convert_int_to_symbol(result)
                answer.append(result)

        answer = ''.join(answer)
        print(answer)
