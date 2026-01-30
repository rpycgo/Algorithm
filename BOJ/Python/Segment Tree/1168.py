import sys


input = sys.stdin.readline
print = sys.stdout.write


class SegmentTree:
    def __init__(self, N):
        self.N = N

        self.h = (N-1).bit_length()
        self.size = 1 << self.h

        self.tree = [0] * (2*self.size)

        self._build()

    def _build(self):
        for i in range(self.N):
            self.tree[self.size+i] = 1

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def query(self, k):
        idx = 1
        while idx < self.size:
            if self.tree[2*idx] >= k:
                idx *= 2
            else:
                k -= self.tree[2*idx]
                idx = 2*idx + 1

        return idx - self.size

    def update(self, target_idx, val):
        target_idx += self.size
        self.tree[target_idx] = val

        while target_idx > 1:
            target_idx //= 2

            self.tree[target_idx] = self.tree[2*target_idx] + self.tree[2*target_idx + 1]


def main():
    N, K = map(int, input().split())

    segment_tree = SegmentTree(N)

    answer = []
    curr_idx = 1

    for i in range(N, 0, -1):
        curr_idx = (curr_idx+K-2)%i + 1

        delete_idx = segment_tree.query(curr_idx)
        answer.append(str(delete_idx+1))

        segment_tree.update(delete_idx, 0)

    print('<' + ', '.join(answer) + '>\n')


if __name__ == '__main__':
    main()
