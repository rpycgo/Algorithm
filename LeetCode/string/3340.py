class Solution:
    def isBalanced(self, num: str) -> bool:
        total_even = sum([int(digit) for i, digit in enumerate(num) if i%2 == 0])
        total_odd = sum([int(digit) for i, digit in enumerate(num) if i%2 == 1])

        answer = True if total_even == total_odd else False

        return answer
