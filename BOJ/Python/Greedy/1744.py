import sys


input = sys.stdin.readline


def main():
    N = int(input())
    
    pos = []
    neg = []
    n_ones = 0

    for _ in range(N):
        num = int(input())

        if num > 1:
            pos.append(num)
        elif num <= 0:
            neg.append(num)
        else:
            n_ones += 1

    pos.sort(reverse=True)
    neg.sort()

    result = n_ones

    for i in range(0, len(pos), 2):
        if i + 1 < len(pos):
            result += pos[i] * pos[i+1]
        else:
            result += pos[i]

    for i in range(0, len(neg), 2):
        if i + 1 < len(neg):
            result += neg[i] * neg[i+1]
        else:
            result += neg[i]

    print(result)


if __name__ == '__main__':
    main()
