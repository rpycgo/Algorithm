class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        hex_map = '0123456789abcdef'
        num &= 0xFFFFFFFF

        answer = []
        while num > 0:
            digit = num & 15

            answer.append(hex_map[digit])

            num >>= 4

        answer = ''.join(reversed(answer))

        return answer
