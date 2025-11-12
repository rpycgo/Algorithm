class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start_map = defaultdict(int)
        end_map = defaultdict(int)

        longest_substring = -1
        for i, char in enumerate(s):
            if char in start_map:
                end_map[char] = i

                diff = end_map[char] - start_map[char] - 1

                if longest_substring < diff:
                    longest_substring = diff
            else:
                start_map[char] = i

        return longest_substring
