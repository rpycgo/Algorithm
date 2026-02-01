class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for val in num:
            while k and stack and val < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(val)

        if k > 0:
            stack = stack[:-k]

        answer = ''.join(stack).lstrip('0')
        answer = answer if answer else '0'

        return answer
