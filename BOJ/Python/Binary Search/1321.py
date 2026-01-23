import sys


input = sys.stdin.readline


def update(i, diff, N, tree):
    while i <= N:
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
    units = [0] + list(map(int, input().split()))

    tree = [0] * (N+1)
    for i in range(1, N+1):
        update(i, units[i], N, tree)

    M = int(input())
    for _ in range(M):
        query = tuple(map(int, input().split()))

        if query[0] == 1:
            update(query[1], query[2], N, tree)
        else:
            target = query[1]

            left, right = 1, N
            answer = N

            while left <= right:
                mid = (left + right) // 2

                if get_sum(mid, tree) >= target:
                    answer = mid
                    right = mid -1
                else:
                    left = mid + 1

            print(answer)


if __name__ == '__main__':
    main()
