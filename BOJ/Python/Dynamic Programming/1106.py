import sys


input = sys.stdin.readline


def main():
    C, N = map(int, input().split())
    ads = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    max_c = C + 100
    dp = [float('inf')] * (max_c+1)
    dp[0] = 0

    for cost, people in ads:
        for i in range(people, max_c+1):
            if dp[i-people] != float('inf'):
                dp[i] = min(dp[i], dp[i-people]+cost)

    answer =  min(dp[C:])
    print(answer)


if __name__ == '__main__':
    main()
