import sys


def router_install(array: list, N: int, M: int) -> int:
    if M == 2:
        return array[N-1] - array[0]

    left = 1
    right = max(array) - 1

    while left <= right:
        mid = (left+right) // 2
        count = 1
        wifi = min(array) + mid

        for i in range(1, len(array)):
            if wifi <= array[i]:
                count +=1
                wifi = array[i] + mid

        if count >= M:
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int, input().split())
    houses = [int(input()) for _ in range(N)]
    houses.sort()

    print(router_install(houses, N, M))
