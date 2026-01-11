import sys
from bisect import bisect_right


sys.setrecursionlimit(4000001)


def find(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_a] = root_b


def main():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    card_numbers = list(map(int, input().split()))
    chulsoo_cards = list(map(int, input().split()))

    card_numbers.sort()

    parent = list(range(M + 1))

    results = []
    for chulsoo_card in chulsoo_cards:
        idx = bisect_right(card_numbers, chulsoo_card)

        available_idx = find(parent, idx)

        results.append(str(card_numbers[available_idx]))
        union(parent, available_idx, available_idx+1)

    answer = '\n'.join(results)

    print(answer)


if __name__ == '__main__':
    main()
