import sys


input = sys.stdin.readline


def main():
    expression = input().rstrip()

    stack = []
    for char in expression:
        if char.isdecimal():
            stack.append(int(char))
        else:
            prev_num = stack.pop()
            prev_prev_num = stack.pop()

            if char == '*':
                result = prev_prev_num * prev_num
            elif char == '/':
                result = prev_prev_num // prev_num
            elif char == '+':
                result = prev_prev_num + prev_num
            elif char == '-':
                result = prev_prev_num - prev_num

            stack.append(result)

    answer = stack[-1]
    print(answer)


if __name__ == '__main__':
    main()
