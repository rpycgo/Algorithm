class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        previous_value = 0
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for symbol in reversed(s):
            value = mapping.get(symbol)

            if value < previous_value:
                total -= value
            else:
                total += value

            previous_value = value

        return total
