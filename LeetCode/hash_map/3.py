class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_index = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in character_index and character_index[char] >= left:
                left = character_index[char] + 1

            character_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
