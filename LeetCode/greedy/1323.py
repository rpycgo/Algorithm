class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        i = -1

        for idx, char in enumerate(s):
            if char == '6':
                i = idx

                break

        if i == -1:
            return num

        s[i] = '9'

        return int(''.join(s))
