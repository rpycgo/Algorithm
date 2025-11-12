class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start_map = {}
        longest_substring = -1

        for i, char in enumerate(s):
            if char in start_map:
                diff = i - start_map[char] - 1

                if diff > longest_substring:
                    longest_substring = diff
            else:
                start_map[char] = i

        return longest_substring
