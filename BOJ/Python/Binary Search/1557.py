import sys


def count_non_square(X, mu):
    cnt = 0
    i = 1

    while i*i <= X:
        cnt += mu[i] * (X // (i * i))
        i += 1

    return cnt


def main():
    K = int(input())

    MAX = 1_000_000
    mu = [0] * MAX
    mu[1] = 1
    for i in range(1, MAX):
        for j in range(i*2, MAX, i):
            mu[j] -= mu[i]

    left = 1
    right = 2_000_000_000
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if count_non_square(mid, mu) >= K:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
