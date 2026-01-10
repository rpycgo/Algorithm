class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y

        answer = 0
        while diff:
            diff &= (diff-1)
            answer += 1

        return answer
