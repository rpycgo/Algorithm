def main():
    string = input()
    string = string + ' '

    stack = []
    is_sign = False
    for char in string:
        if char == '<':
            is_sign = True

            print(''.join(stack)[::-1] if stack else '', sep='', end='')

            stack.clear()

            stack.append(char)
        elif char == '>':
            is_sign = False

            stack.append(char)

            print(''.join(stack), sep='', end='')

            stack.clear()
        elif char == ' ' and not is_sign:
            print(''.join(stack)[::-1], sep='', end=' ')

            stack.clear()
        else:
            stack.append(char)


if __name__ == '__main__':
    main()
