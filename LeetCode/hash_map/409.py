class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        length = 0
        has_odd = False
        for value in count.values():
            if value%2 == 0:
                length += value
            else:
                length += value-1
                has_odd = True

        if has_odd:
            length += 1

        return length
