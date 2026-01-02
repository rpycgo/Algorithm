class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        count = 9
        start = 1

        while n > digit*count:
            n -= digit*count
            digit += 1
            count *= 10
            start *= 10

        offset = (n-1) // digit
        digit_index = (n-1) % digit

        num = start + offset
        s = str(num)

        answer = int(s[digit_index])

        return answer
