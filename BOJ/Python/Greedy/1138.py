import sys


input = sys.stdin.readline


def main():
    N = int(input())

    info = list(map(int, input().split()))

    result = [0] * N
    for i in range(N):
        n_taller = info[i]
        cnt = 0

        for j in range(N):
            if result[j] == 0:
                if cnt == n_taller:
                    result[j] = i + 1
                    break
                else:
                    cnt += 1
    print(*result)


if __name__ == '__main__':
    main()
