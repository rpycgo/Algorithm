class Solution:
    def countDistinct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        length = len(digits)

        @lru_cache(None)
        def dfs(pos, is_limit, has_started):
            if pos == length:
                return 1 if has_started else 0

            total = 0
            max_digit = digits[pos] if is_limit else 9

            for digit in range(max_digit + 1):
                if digit == 0 and has_started:
                    continue

                total += dfs(
                    pos + 1,
                    is_limit and digit == max_digit,
                    has_started or digit > 0,
                )

            return total

        return dfs(0, True, False)
