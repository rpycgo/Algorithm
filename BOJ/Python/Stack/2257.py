import sys


input = sys.stdin.readline


def main():
    formula = input().rstrip()

    mass = {'H': 1, 'C': 12, 'O': 16}

    stack = []
    for char in formula:
        if char == '(':
            stack.append(char)
        elif char == ')':
            temp_sum = 0
            while True:
                top = stack.pop()

                if top == '(':
                    break

                temp_sum += top
            stack.append(temp_sum)
        elif char in mass:
            stack.append(mass[char])
        else:
            num = int(char)
            stack[-1] *= num

    total_mass = sum(stack)
    print(total_mass)


if __name__ == '__main__':
    main()
