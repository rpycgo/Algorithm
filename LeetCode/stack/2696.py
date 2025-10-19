class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            stack.append(char)

            while len(stack) >= 2 and (''.join(stack[-2:]) == 'AB' or ''.join(stack[-2:]) == 'CD'):            
                stack.pop()
                stack.pop()

        s = ''.join(stack)

        return len(s)
