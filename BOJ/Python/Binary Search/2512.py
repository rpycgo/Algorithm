import sys


def calculate_total_budget(upper_limit, budgets):
    total = 0
    for budget in budgets:
        total += min(upper_limit, budget)

    return total


def main():
    input = sys.stdin.readline

    N = int(input())
    budgets = list(map(int, input().split()))
    M = int(input())

    budgets.sort()

    left = 1
    right = max(budgets)

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_total_budget(mid, budgets) <= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
