import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)


class PostOrder:
    def __init__(self, n, inorder, postorder):
        self.n = n
        self.inorder = inorder
        self.postorder = postorder

        self.position = [0] * (n+1)
        for i in range(n):
            self.position[self.inorder[i]] = i

    def get_preorder(self, in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return

        root = self.postorder[post_end]
        print(root, end=' ')

        root_idx = self.position[root]
        left_count = root_idx - in_start

        self.get_preorder(in_start, root_idx-1, post_start, post_start+left_count-1)
        self.get_preorder(root_idx+1, in_end, post_start+left_count, post_end-1)

    def run(self):
        self.get_preorder(0, self.n-1, 0, self.n-1)


if __name__ == '__main__':
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    PostOrder(n, inorder, postorder).run()
