import sys


def calculate_draw_count(k, budgets):
    draw_count = 1
    current_money = k

    for budget in budgets:
        if current_money < budget:
            draw_count += 1
            current_money = k

        current_money -= budget

    return draw_count


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    budgets = [int(input()) for _ in range(N)]

    left = max(budgets)
    right = N * left

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_draw_count(mid, budgets) > M:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
