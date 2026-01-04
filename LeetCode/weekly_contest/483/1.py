class Solution:
    def largestEven(self, s: str) -> str:
        while len(s) > 0:
            if int(s)%2 == 0:
                return s
            else:
                s = s[:-1]

        return ''
