import sys


def update(tree, i, diff):
    i += 1
    while i < len(tree):
        tree[i] += diff
        i += (i & -i)


def query(tree, i):
    s = 0

    i += 1
    while i > 0:
        s += tree[i]
        i -= (i & -i)

    return s


def find_kth(tree, k):
    low = 0
    high = 65535

    result = 0
    while low <= high:
        mid = (low + high) // 2

        if query(tree, mid) >= k:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    temps = [int(input()) for _ in range(N)]

    tree = [0] * 65537
    mid_idx = (K + 1) // 2
    answer = 0

    for i in range(K-1):
        update(tree, temps[i], 1)

    for i in range(K-1, N):
        update(tree, temps[i], 1)
        answer += find_kth(tree, mid_idx)
        update(tree, temps[i-K+1], -1)

    print(answer)


if __name__ == '__main__':
    main()
