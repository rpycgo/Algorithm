import sys


input = sys.stdin.readline


def main():
    string1 = input().rstrip()
    string2 = input().rstrip()

    n1 = len(string1)
    n2 = len(string2)

    prev = [0] * (n2+1)
    max_len = 0

    for i in range(1, n1+1):
        curr = [0] * (n2+1)
        for j in range(1, n2+1):
            if string1[i-1] == string2[j-1]:
                curr[j] = prev[j-1] + 1

                max_len = max(max_len, curr[j])

        prev = curr

    print(max_len)


if __name__ == '__main__':
    main()
