import sys


def calculate_n_children(n_operation, times):
    count = len(times)
    for time in times:
        n = n_operation // time
        count += n

    return count


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    times = list(map(int, input().split()))

    if N <= M:
        print(N)
        return

    left = 0
    right = 2_000_000_000 * 30
    total_time = 0

    while left <= right:
        mid = (left+right) // 2

        if calculate_n_children(mid, times) >= N:
            total_time = mid
            right = mid - 1
        else:
            left = mid + 1


    cnt = M
    for time in times:
        cnt += (total_time-1) // time

    for i in range(M):
        if total_time % times[i] == 0:
            cnt += 1

            if cnt == N:
                print(i+1)
                return


if __name__ == '__main__':
    main()
