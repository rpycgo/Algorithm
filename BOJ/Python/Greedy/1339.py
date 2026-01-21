import sys


input = sys.stdin.readline


def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]

    alpha_weight = {}
    for word in words:
        n = len(word)
        for i in range(n):
            char = word[i]
            weight = 10 ** (n-i-1)

            if char in alpha_weight:
                alpha_weight[char] += weight
            else:
                alpha_weight[char] = weight

    weights = sorted(alpha_weight.values(), reverse=True)

    total_val = 0
    assigned_num = 9
    for weight in weights:
        total_val += weight * assigned_num
        assigned_num -= 1

    print(total_val)


if __name__ == '__main__':
    main()
