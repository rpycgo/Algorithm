import sys
from collections import Counter


input = sys.stdin.readline


def main():
    name = input().rstrip()

    counts = Counter(name)

    sorted_keys = sorted(counts.keys())

    n_odds = 0
    center = ''
    half_result = ''

    for char in sorted_keys:
        if counts[char]%2 == 1:
            n_odds += 1
            center = char

        if n_odds > 1:
            print("I'm Sorry Hansoo")
            return

        half_result += (char * (counts[char]//2))

    answer = half_result + center + half_result[::-1]
    print(answer)


if __name__ == '__main__':
    main()
