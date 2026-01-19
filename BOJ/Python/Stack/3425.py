import sys


input = sys.stdin.read


def main():
    data = input().split()

    idx = 0
    while True:
        commands = []

        while idx < len(data):
            cmd = data[idx]
            idx += 1

            if cmd == 'QUIT':
                return
            if cmd == 'END':
                break
            if cmd == 'NUM':
                num = data[idx]
                idx += 1

                commands.append(('NUM', int(num)))
            else:
                commands.append((cmd, None))

        n = int(data[idx])
        idx += 1

        for _ in range(n):
            v = int(data[idx])
            idx += 1

            stack = [v]
            error = False

            for cmd, arg in commands:
                if cmd == 'NUM':
                    stack.append(arg)
                elif not stack:
                    error = True
                    break
                elif cmd == 'POP':
                    stack.pop()
                elif cmd == 'INV':
                    stack[-1] = -stack[-1]
                elif cmd == 'DUP':
                    stack.append(stack[-1])
                else:
                    if len(stack) < 2:
                        error = True
                        break

                    b = stack.pop()
                    a = stack.pop()

                    res = 0
                    if cmd == 'SWP':
                        stack.append(b)
                        stack.append(a)
                        continue
                    elif cmd == 'ADD':
                        res = a + b
                    elif cmd == 'SUB':
                        res = a - b
                    elif cmd == 'MUL':
                        res = a * b
                    elif cmd == 'DIV':
                        if b == 0:
                            error = True
                            break

                        res = abs(a) // abs(b)

                        if (a < 0) ^ (b < 0):
                            res = -res
                    elif cmd == 'MOD':
                        if b == 0:
                            error = True
                            break

                        res = abs(a) % abs(b)

                        if a < 0:
                            res = -res

                    if abs(res) > 10**9:
                        error = True
                        break

                    stack.append(res)

            if error or len(stack) != 1:
                print("ERROR")
            else:
                print(stack[0])
        print()


if __name__ == '__main__':
    main()
