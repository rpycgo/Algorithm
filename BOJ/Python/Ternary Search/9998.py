import sys


input = sys.stdin.readline


def cal_cost(h, n, dong, yoon):
    cost = 0

    mid = n // 2
    for i in range(n):
        target = h + abs(mid - i)

        cost += abs(dong[i] - target)
        cost += abs(yoon[i] - target)

    return cost


def main():
    N = int(input())
    block_heights_yoon = list(map(int, input().split()))
    block_heights_dong = list(map(int, input().split()))

    low = 0
    high = 10 ** 12

    while high - low >= 3:
        p1 = (low*2 + high) // 3
        p2 = (low + high*2) // 3

        if cal_cost(p1, N, block_heights_yoon, block_heights_dong) <= cal_cost(p2, N, block_heights_yoon, block_heights_dong):
            high = p2
        else:
            low = p1

    min_cost = cal_cost(low, N, block_heights_yoon, block_heights_dong)
    for h in range(low+1, high+1):
        curr_cost = cal_cost(h, N, block_heights_yoon, block_heights_dong)
        if min_cost > curr_cost:
            min_cost = curr_cost

    print(min_cost)


if __name__ == '__main__':
    main()
