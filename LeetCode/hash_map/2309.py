class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)
        for char in reversed('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            if char in chars and char.lower() in chars:
                return char

        return ''
