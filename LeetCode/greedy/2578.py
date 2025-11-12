class Solution:
    def splitNum(self, num: int) -> int:
        num = list(str(num))
        num.sort()

        num1, num2 = num[::2], num[1::2]

        num1 = int(''.join(num1))
        num2 = int(''.join(num2))

        answer = num1 + num2

        return answer
