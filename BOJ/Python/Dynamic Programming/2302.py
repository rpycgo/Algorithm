import sys


input = sys.stdin.readline


def main():
    N = int(input())

    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1

    if N >= 2:
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]

    M = int(input())
    vip_positions = [int(input()) for _ in range(M)]

    answer = 1
    last_pos = 0

    for vip_position in vip_positions:
        section_len = vip_position - last_pos - 1
        answer *= dp[section_len]
        last_pos = vip_position

    final_section_len = N - last_pos
    answer *= dp[final_section_len]

    print(answer)


if __name__ == '__main__':
    main()
