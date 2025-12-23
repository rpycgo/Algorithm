class Solution:
    def mirrorDistance(self, n: int) -> int:
        str_n = str(n)
        str_reversed = int(str_n[::-1])

        answer = abs(str_reversed - n)

        return answer
