import sys


input = sys.stdin.readline


def solve(n, P, Q, cache):
    if n in cache:
        return cache[n]

    cache[n] = solve(n//P, P, Q, cache) + solve(n//Q, P, Q, cache)

    return cache[n]


def main():
    N, P, Q = map(int, input().split())

    cache = {0: 1}

    answer = solve(N, P, Q, cache)
    print(answer)


if __name__ == '__main__':
    main()
