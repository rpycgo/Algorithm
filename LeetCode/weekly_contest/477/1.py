class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [char for char in str(n) if char != '0']

        if not digits:
            return 0

        number = int(''.join(digits))
        total = sum([int(digit) for digit in digits])

        answer = number * total

        return answer
