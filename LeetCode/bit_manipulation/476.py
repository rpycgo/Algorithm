class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()

        mask = (1 << bit_length) -1

        answer = num ^ mask

        return answer
