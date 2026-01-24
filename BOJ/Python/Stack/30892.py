import sys


input = sys.stdin.readline


def main():
    N, K, T = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    stack = []
    idx = 0

    for _ in range(K):
        while idx < N and A[idx] < T:
            stack.append(A[idx])
            idx += 1

        if stack:
            T += stack.pop()
        else:
            break

    print(T)


if __name__ == '__main__':
    main()
