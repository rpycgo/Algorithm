class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n+1):
            if not self.has_zero(i) and not self.has_zero(n-i):
                return [i, n-i]

    def has_zero(self, number):
        number = str(number)

        return True if '0' in number else False
