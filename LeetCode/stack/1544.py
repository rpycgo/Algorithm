class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s

        stack = [s[0]]
        i = 1
        while i != len(s):
            if stack and stack[-1] != s[i] and (stack[-1] == s[i].lower() or stack[-1] == s[i].upper()):
                stack.pop()
            else:
                stack.append(s[i])

            i += 1

        return ''.join(stack)
