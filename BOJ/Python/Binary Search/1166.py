import sys


def main():
    N, L, W, H = map(int, input().split())

    left = 0
    right = max(L, W, H)

    for _ in range(100):
        mid = (left+right) / 2

        count = int(L/mid) * int(W/mid) * int(H/mid)
        if count >= N:
            left = mid
        else:
            right = mid

    print(f'{right:.10f}')


if __name__ == '__main__':
    main()
