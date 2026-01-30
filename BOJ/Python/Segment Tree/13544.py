import sys
from bisect import bisect_right


input = sys.stdin.readline


class MergeSortTree:
    def __init__(self, N, A):
        self.N = N
        self.A = A

        self.h = N.bit_length()
        self.size = 1 << self.h

        self.tree = [[] for _ in range(2*self.size)]

        self._build()

    def _build(self):
        for i, a in enumerate(self.A):
            self.tree[i+self.size] = [self.A[i]]

        for i in range(self.size-1, 0, -1):
            self.tree[i] = sorted(self.tree[2*i] + self.tree[2*i + 1])

    def query(self, left, right, k):
        left += self.size
        right += self.size

        cnt = 0
        while left <= right:
            if left%2 == 1:
                node_list =  self.tree[left]
                cnt += len(node_list) - bisect_right(node_list, k)
                left += 1

            if right%2 == 0:
                node_list = self.tree[right]
                cnt += len(node_list) - bisect_right(node_list, k)
                right -= 1

            left //= 2
            right //= 2

        return cnt


def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    M = int(input())

    last_ans = 0
    segment_tree = MergeSortTree(N, A)

    for _ in range(M):
        a, b, c = map(int, input().split())

        i = a ^ last_ans
        j = b ^ last_ans
        k = c ^ last_ans

        answer = segment_tree.query(i-1, j-1, k)
        print(answer)

        last_ans = answer


if __name__ == '__main__':
    main()
