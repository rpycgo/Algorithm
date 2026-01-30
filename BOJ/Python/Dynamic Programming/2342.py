import sys


input = sys.stdin.readline


def get_cost(start, end):
    if start == 0:
        return 2
    if start == end:
        return 1
    if abs(start-end) == 2:
        return 4
    return 3


def main():
    seqs = list(map(int, input().split()))

    if seqs[0] == 0:
        print(0)
        return

    dp = {(0, 0): 0}

    for target in seqs:
        if target == 0:
            break

        next_dp = {}

        for (left, right), cost in dp.items():
            if target != right:
                new_cost = cost + get_cost(left, target)

                if ((target, right) not in next_dp) or (new_cost < next_dp[(target, right)]):
                    next_dp[(target, right)] = new_cost

            if target != left:
                new_cost = cost + get_cost(right, target)

                if ((left, target) not in next_dp) or (new_cost < next_dp[(left, target)]):
                    next_dp[(left, target)] = new_cost

        dp = next_dp

    answer = min(dp.values())
    print(answer)


if __name__ == '__main__':
    main()
