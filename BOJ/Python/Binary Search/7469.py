import sys
from bisect import bisect_right


def build(node, start, end, a, tree):
    if start == end:
        tree[node] = [a[start]]
        return

    mid = (start + end) // 2
    build(node*2, start, mid, a, tree)
    build(node*2 + 1, mid+1, end, a, tree)

    tree[node] = sorted(tree[node*2] + tree[node*2 + 1])


def get_count(node, start, end, i, j, val, tree):
    if j < start or end < i:
        return 0
    if i <= start and end <= j:
        return bisect_right(tree[node], val)

    mid = (start + end) // 2

    return get_count(node*2, start, mid, i, j, val, tree) + \
           get_count(node*2+1, mid+1, end, i, j, val, tree)


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    tree = [[] for _ in range(4 * n)]
    build(1, 0, n-1, a, tree)

    a.sort()

    for _ in range(m):
        i, j, k = map(int, input().split())

        low = 0
        high = n - 1
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            val = a[mid]

            if get_count(1, 0, n-1, i-1, j-1, val, tree) >= k:
                answer = val
                high = mid - 1
            else:
                low = mid + 1

        print(answer)


if __name__ == '__main__':
    main()
