import sys


input = sys.stdin.readline


def update(i, diff, N, tree):
    while i < N:
        tree[i] += diff
        i += (i & -i)


def get_sum(i, tree):
    total = 0
    while i > 0:
        total += tree[i]
        i -= (i & -i)

    return total


def main():
    N = int(input())
    A = list(map(int, input().split()))

    tree = [0] * (N+1)
    answer = [0] * (N+1)

    for i in range(1, N+1):
        update(i, 1, N, tree)

    for i in range(N, 0, -1):
        a = A[i-1]

        total_empty = i
        target = total_empty - a

        left = 1
        right = N
        pos = N

        while left <= right:
            mid = (left + right) // 2

            if get_sum(mid, tree) >= target:
                pos = mid
                right = mid -1
            else:
                left = mid + 1

        answer[pos] = i
        update(pos, -1, N, tree)

    answer = ' '.join(map(str, answer[1:]))
    print(answer)


if __name__ == '__main__':
    main()
