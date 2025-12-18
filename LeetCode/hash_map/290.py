class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern2word = {}
        word2pattern = {}

        for char, word in zip(pattern, words):
            if char in pattern2word and pattern2word[char] != word:
                return False
            if word in word2pattern and word2pattern[word] != char:
                return False

            pattern2word[char] = word
            word2pattern[word] = char

        return True
