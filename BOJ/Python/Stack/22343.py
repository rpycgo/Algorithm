import sys


input = sys.stdin.readline


def calculate_function_value(string):
    bits = [0] * (len(string)+1)
    depth = 0

    for i, char in enumerate(string):
        if char == '(':
            depth += 1
        else:
            depth -= 1

            if string[i-1] == '(':
                bits[depth] += 1

    for i in range(len(bits)-1):
        bits[i+1] += bits[i]//2
        bits[i] %= 2

    return bits


def compare(A_bits, B_bits):
    max_len = max(len(A_bits), len(B_bits))

    for i in range(max_len - 1, -1, -1):
        a = A_bits[i] if i < len(A_bits) else 0
        b = B_bits[i] if i < len(B_bits) else 0

        if a > b:
            return '>'
        if a < b:
            return '<'
    return '='


def main():
    T = int(input())
    for _ in range(T):
        A = input().rstrip()
        B = input().rstrip()

        val_A = calculate_function_value(A)
        val_B = calculate_function_value(B)

        answer = compare(val_A, val_B)
        print(answer)


if __name__ == '__main__':
    main()
