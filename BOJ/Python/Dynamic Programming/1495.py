import sys


input = sys.stdin.readline


def solve(idx, curr_sum, M, volumes, dp):
    if curr_sum < 0 or curr_sum > M:
        return -2

    if idx == len(volumes):
        return curr_sum

    if dp[idx][curr_sum] != -1:
        return dp[idx][curr_sum]

    cnt = -2
    cnt = max(cnt, solve(idx+1, curr_sum+volumes[idx], M, volumes, dp))
    cnt = max(cnt, solve(idx+1, curr_sum-volumes[idx], M, volumes, dp))

    dp[idx][curr_sum] = cnt

    return cnt


def main():
    N, S, M = map(int, input().split())
    volumes = tuple(map(int, input().split()))

    dp = [[-1] * (M+1) for _ in range(N+1)]

    cnt = solve(0, S, M, volumes, dp)
    answer = -1 if cnt == -2 else cnt
    print(answer)


if __name__ == '__main__':
    main()
