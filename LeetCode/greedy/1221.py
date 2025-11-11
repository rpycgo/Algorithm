class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l = 0
        count_r = 0
        answer = 0

        for char in s:
            if char == 'L':
                count_l += 1
            else:
                count_r += 1

            if count_l == count_r:
                answer += 1

        return answer
