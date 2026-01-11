import sys
from bisect import bisect_left, bisect_right


def get_all_sums(pizza, n):
    sums = [0]

    total = sum(pizza)
    sums.append(total)

    pizza_circled = pizza + pizza
    for i in range(n):
        temp = 0
        for j in range(n-1):
            temp += pizza_circled[i+j]
            sums.append(temp)

    return sums


def main():
    input = sys.stdin.readline

    target = int(input())
    m, n = map(int, input().split())
    sizes_A = [int(input()) for _ in range(m)]
    sizes_B = [int(input()) for _ in range(n)]

    sums_A = get_all_sums(sizes_A, m)
    sums_B = get_all_sums(sizes_B, n)

    sums_B.sort()

    answer = 0
    for sum_a in sums_A:
        remaining = target - sum_a
        if remaining < 0:
            continue

        count = bisect_right(sums_B, remaining) - bisect_left(sums_B, remaining)
        answer += count

    print(answer)


if __name__ == '__main__':
    main()
