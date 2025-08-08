class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        previous_character = ''
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for symbol in s:
            if previous_character == 'I' and symbol in ('V', 'X'):
                total -= mapping.get(previous_character)*2
            elif previous_character == 'X' and symbol in ('L', 'C'):
                total -= mapping.get(previous_character)*2
            elif previous_character == 'C' and symbol in ('D', 'M'):
                total -= mapping.get(previous_character)*2

            total += mapping.get(symbol)
            previous_character = symbol

        return total
