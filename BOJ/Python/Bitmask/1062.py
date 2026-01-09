import sys
from itertools import combinations


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())

    if K < 5:
        print(0)
        return
    if K == 26:
        print(N)
        return

    words = []
    for _ in range(N):
        word = input().strip()

        bit = 0
        for char in word:
            bit |= (1 << (ord(char) - ord('a')))
        words.append(bit)

    essential = 0
    for char in ['a', 'n', 't', 'i', 'c']:
        essential |= (1 << (ord(char) - ord('a')))

    candidates = [1 << i for i in range(26) if not (essential & (1 << i))]

    max_count = 0
    for extra in combinations(candidates, K-5):
        learned = essential

        for bit in extra:
            learned |= bit

        count = 0
        for word_bit in words:
            if (word_bit & learned) == word_bit:
                count += 1

        max_count = max(max_count, count)

    print(max_count)


if __name__ == '__main__':
    main()
    