import sys


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    counts = [0] * M
    prefix = 0

    for num in numbers:
        prefix = (prefix + num) % M
        counts[prefix] += 1

    answer = counts[0]
    for count in counts:
        if count >= 2:
            answer += (count*(count-1) // 2)

    print(answer)


if __name__ == '__main__':
    main()
