class Solution:
    def digitCount(self, num: str) -> bool:
        count = defaultdict(int)

        for digit in num:
            count[digit] += 1

        for i, num in enumerate(num):
            if int(num) != count[str(i)]:
                return False

        return True
