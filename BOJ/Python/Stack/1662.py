import sys


input = sys.stdin.readline


def main():
    S = input().rstrip()

    stack = []
    for char in S:
        if char == '(':
            _, K = stack.pop()
            stack.append((K, 'K'))
            stack.append(('(', '('))
        elif char == ')':
            curr_len = 0
            while True:
                val, type = stack.pop()

                if type == '(':
                    break

                curr_len += val

            K, _ = stack.pop()
            stack.append((K*curr_len, 'LEN'))
        else:
            stack.append((1, int(char)))

    total_len = 0
    for val, type in stack:
        total_len += val

    print(total_len)


if __name__ == '__main__':
    main()
