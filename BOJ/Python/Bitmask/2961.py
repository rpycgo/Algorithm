import sys


input = sys.stdin.readline


def main():
    N = int(input())
    ingredients = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    min_diff = float('inf')
    for i in range(1, 1 << N):
        sour_total = 1
        bitter_total = 0

        for j in range(N):
            if i & (1 << j):
                sour_total *= ingredients[j][0]
                bitter_total += ingredients[j][1]

        diff = abs(sour_total - bitter_total)
        if diff < min_diff:
            min_diff = diff

    print(min_diff)


if __name__ == '__main__':
    main()
