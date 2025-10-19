class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if stack:
                top = stack[-1]

                if (top == 'A' and char == 'B') or (top == 'C' and char == 'D'):
                    stack.pop()
                    continue

            stack.append(char)

        return len(stack)