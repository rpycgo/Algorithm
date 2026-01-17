import sys


input = sys.stdin.readline


def main():
    S = input().rstrip()

    len_s = len(S)

    unique_chars = set(S)
    prefix_map = {char: [0] * (len_s + 1) for char in unique_chars}

    for i, char in enumerate(S):
        for unique_char in unique_chars:
            prefix_map[unique_char][i+1] = prefix_map[unique_char][i]
        prefix_map[char][i+1] += 1

    q = int(input())
    for _ in range(q):
        alpha, l, r = input().split()

        l = int(l)
        r = int(r)

        if alpha not in prefix_map:
            print('0')
        else:
            answer = prefix_map[alpha][r+1] - prefix_map[alpha][l]
            print(answer)


if __name__ == '__main__':
    main()
