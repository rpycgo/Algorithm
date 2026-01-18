import sys


sys.setrecursionlimit(10**6)


class PostOrder:
    def __init__(self, n, pre_order, in_order):
        self.n = n
        self.pre_order = pre_order
        self.in_order = in_order

        self.positions = [0] * (n + 1)
        for i in range(n):
            self.positions[self.in_order[i]] = i

    def find_post_order(self, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return

        root = self.pre_order[pre_start]

        root_idx = self.positions[root]
        left_cnt = root_idx - in_start

        self.find_post_order(pre_start+1, pre_start+left_cnt, in_start, root_idx-1)
        self.find_post_order(pre_start+left_cnt+1, pre_end, root_idx+1, in_end)

        print(root, end=' ')

    def run(self):
        self.find_post_order(0, self.n-1, 0, self.n-1)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        pre_order = list(map(int, input().split()))
        in_order = list(map(int, input().split()))

        post_order = PostOrder(n, pre_order, in_order)
        post_order.run()
        print()
