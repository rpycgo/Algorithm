def solution(string: str, exploding_string: str):
    stack = []
    length = len(exploding_string)
    for char in string:
        stack.append(char)

        if ''.join(stack[-length:]) == exploding_string:
            for _ in range(length):
                stack.pop()

    return ''.join(stack) if stack else 'FRULA'


if __name__ == '__main__':
    string = input()
    exploding_string = input()

    print(solution(string, exploding_string))
