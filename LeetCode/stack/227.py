class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        stack = []
        num = 0
        sign = '+'

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    prev = stack.pop()

                    if prev // num < 0 and prev % num != 0:
                        stack.append(prev // num + 1)
                    else:
                        stack.append(prev // num)

                sign = char
                num = 0

        return sum(stack)
