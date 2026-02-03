import sys


input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    T = tuple(map(int, input().split()))

    prefix_sums = [0] * (n+1)
    for i in range(n):
        prefix_sums[i+1] = prefix_sums[i] + T[i]

    max_wage = float('-inf')
    for i in range(n-m+1):
        wage = prefix_sums[i+m] - prefix_sums[i]

        max_wage = max(max_wage, wage)

    print(max_wage)


if __name__ == '__main__':
    main()
